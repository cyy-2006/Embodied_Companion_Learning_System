"""MuJoCo 智慧教室仿真世界（宇树 G1 29-DoF）。

- 模型：MuJoCo Menagerie `unitree_g1` 官方 MJCF（29 个 position 伺服电机）
- 场景：原 Three.js 教室 GLTF 转出的 OBJ 网格（仅渲染/射线，不参与接触）
- 控制：29 电机位置伺服 + 程序化步态；浮动基座由控制器推进（无预训练行走策略）
- 传感器：头部 D435 相机（`mujoco.Renderer` + 固定相机 `head_cam`）、Mid-360 2D 雷达（`mj_ray`）

坐标系与 PyBullet 版本一致：X 前向，Y 左向，Z 向上，地面 z=0。
"""
import io
import json
import math
import os
import threading
import time

import mujoco
import numpy as np
from PIL import Image

from . import config
from .planner import GridMap, wrap_angle


# 宇树 G1 官方 stand 关键帧：双臂微屈、双腿伸直
STAND_POSE = {
    "left_shoulder_pitch_joint": 0.20,
    "right_shoulder_pitch_joint": 0.20,
    "left_shoulder_roll_joint": 0.20,
    "right_shoulder_roll_joint": -0.20,
    "left_elbow_joint": 1.28,
    "right_elbow_joint": 1.28,
}

MAX_OBSTACLES = 24


class MjClassroomSim:
    def __init__(self, base_dir):
        self.base_dir = os.path.abspath(base_dir)
        self.lock = threading.RLock()
        self._stop = False
        self._thread = None

        scene = os.path.join(self.base_dir, "assets", "mujoco", "scene.xml")
        self.model = mujoco.MjModel.from_xml_path(scene)
        self.data = mujoco.MjData(self.model)
        self.model.opt.timestep = 1.0 / config.PHYSICS_HZ

        with open(
            os.path.join(self.base_dir, "assets", "scene_meta.json"), "r", encoding="utf-8"
        ) as f:
            self.meta = json.load(f)

        # ---------------------------------------------------------- 模型索引
        self.classroom_gid = self._geom_id("classroom_geom")
        self.floor_gid = self._geom_id("floor")
        self.camera_id = mujoco.mj_name2id(
            self.model, mujoco.mjtObj.mjOBJ_CAMERA, "head_cam"
        )
        self.lidar_site = mujoco.mj_name2id(
            self.model, mujoco.mjtObj.mjOBJ_SITE, "lidar_site"
        )
        self.obstacle_gids = [self._geom_id(f"obstacle_{i}") for i in range(MAX_OBSTACLES)]

        # 29 个位置伺服电机（名称与关节一致）
        self.actuators = {}
        self.joint_qpos = {}
        for i in range(self.model.nu):
            name = mujoco.mj_id2name(self.model, mujoco.mjtObj.mjOBJ_ACTUATOR, i)
            if not name:
                continue
            self.actuators[name] = i
            jid = mujoco.mj_name2id(self.model, mujoco.mjtObj.mjOBJ_JOINT, name)
            self.joint_qpos[name] = int(self.model.jnt_qposadr[jid])

        # 射线只看 group 1（教室 / 地面 / 障碍物），忽略机器人自身
        self.ray_filter = np.zeros(6, dtype=np.uint8)
        self.ray_filter[1] = 1
        self._ray_geom = np.array([-1], dtype=np.int32)
        self._ray_pnt = np.zeros(3, dtype=np.float64)
        self._ray_vec = np.zeros(3, dtype=np.float64)

        # ---------------------------------------------------------- 运行状态
        self.gait_phase = 0.0
        self.gait_amp = 0.0
        self.cmd_v = 0.0
        self.cmd_w = 0.0
        self.obstacles = []
        self._target_pose = (0.0, 0.0, 0.0)
        self.path = []
        self.path_index = 0
        self.navigating = False
        self.arrived = False
        self.teleop_v = 0.0
        self.teleop_w = 0.0
        self.teleop_time = 0.0
        self.lidar_points = []
        self._last_lidar_time = 0.0
        self._camera_bytes = b""
        self._camera_time = 0.0
        self._renderer = None
        self._state = {}

        with self.lock:
            self._prepare_world()
            spawn = self._find_spawn()
            self.spawn = (spawn[0], spawn[1], config.HUMANOID_BASE_Z)
            self._reset_pose()
            # 预热离屏渲染：首次创建 OSMesa 上下文约需数秒，避免首个相机请求卡住主循环
            try:
                self.render_camera()
            except Exception as exc:
                print(f"[sim] 相机渲染初始化失败：{exc}")

        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()

    # ------------------------------------------------------------------ setup
    def _geom_id(self, name):
        gid = mujoco.mj_name2id(self.model, mujoco.mjtObj.mjOBJ_GEOM, name)
        if gid < 0:
            raise RuntimeError(f"场景缺少 geom: {name}")
        return gid

    def _prepare_world(self):
        """计算教室自身的静态占用栅格（障碍物在其上叠加）。"""
        mujoco.mj_forward(self.model, self.data)
        bounds = self.meta["bullet_bounds"]
        self._grid_min_x = bounds[0][0] + config.GRID_MARGIN
        self._grid_min_y = bounds[0][1] + config.GRID_MARGIN
        max_x = bounds[1][0] - config.GRID_MARGIN
        max_y = bounds[1][1] - config.GRID_MARGIN
        self._grid_nx = int(math.ceil((max_x - self._grid_min_x) / config.CELL_SIZE))
        self._grid_ny = int(math.ceil((max_y - self._grid_min_y) / config.CELL_SIZE))

        blocked = np.zeros((self._grid_nx, self._grid_ny), dtype=bool)
        for ix in range(self._grid_nx):
            x = self._grid_min_x + (ix + 0.5) * config.CELL_SIZE
            for iy in range(self._grid_ny):
                y = self._grid_min_y + (iy + 0.5) * config.CELL_SIZE
                gid, z = self._ray_down(x, y)
                if gid == self.classroom_gid and z > 0.10:
                    blocked[ix, iy] = True

        self._base_blocked = blocked
        self._rebuild_grid()

    def _ray_down(self, x, y):
        self._ray_pnt[:] = (x, y, 1.8)
        self._ray_vec[:] = (0.0, 0.0, -1.8)
        self._ray_geom[0] = -1
        distance = mujoco.mj_ray(
            self.model, self.data, self._ray_pnt, self._ray_vec,
            self.ray_filter, True, -1, self._ray_geom,
        )
        gid = int(self._ray_geom[0])
        if gid < 0:
            return -1, 0.0
        return gid, 1.8 - distance * 1.8

    def _rebuild_grid(self):
        blocked = self._base_blocked.copy()
        for item in self.obstacles:
            ix0 = max(0, int(math.floor((item["min_x"] - self._grid_min_x) / config.CELL_SIZE)))
            ix1 = min(
                self._grid_nx - 1,
                int(math.floor((item["max_x"] - self._grid_min_x) / config.CELL_SIZE)),
            )
            iy0 = max(0, int(math.floor((item["min_y"] - self._grid_min_y) / config.CELL_SIZE)))
            iy1 = min(
                self._grid_ny - 1,
                int(math.floor((item["max_y"] - self._grid_min_y) / config.CELL_SIZE)),
            )
            if ix0 <= ix1 and iy0 <= iy1:
                blocked[ix0:ix1 + 1, iy0:iy1 + 1] = True

        blocked = self._inflate(
            blocked, int(math.ceil(config.INFLATE_RADIUS / config.CELL_SIZE))
        )
        blocked[0, :] = True
        blocked[-1, :] = True
        blocked[:, 0] = True
        blocked[:, -1] = True
        self.grid = GridMap(blocked, self._grid_min_x, self._grid_min_y, config.CELL_SIZE)

    @staticmethod
    def _inflate(blocked, radius_cells):
        out = blocked.copy()
        src = np.argwhere(blocked)
        nx, ny = blocked.shape
        for ix, iy in src:
            x0, x1 = max(0, ix - radius_cells), min(nx, ix + radius_cells + 1)
            y0, y1 = max(0, iy - radius_cells), min(ny, iy + radius_cells + 1)
            out[x0:x1, y0:y1] = True
        return out

    def _find_spawn(self):
        ix, iy = self.grid.world_to_cell(1.4, 0.0)
        free = self.grid.nearest_free(ix, iy, max_cells=80)
        if free is None:
            return self.grid.cell_to_world(self.grid.nx // 2, self.grid.ny // 2)
        return self.grid.cell_to_world(*free)

    def _reset_pose(self):
        mujoco.mj_resetDataKeyframe(self.model, self.data, 0)
        for name, index in self.actuators.items():
            self.data.ctrl[index] = STAND_POSE.get(name, 0.0)
        x, y, _ = self.spawn
        self._target_pose = (x, y, 0.0)
        self._hold_base(x, y, 0.0)
        mujoco.mj_forward(self.model, self.data)
        self._update_lidar()
        self._update_state()

    def _hold_base(self, x, y, yaw):
        z = config.HUMANOID_BASE_Z + config.STEP_BOB * abs(math.sin(self.gait_phase))
        self.data.qpos[0] = x
        self.data.qpos[1] = y
        self.data.qpos[2] = z
        half = yaw * 0.5
        self.data.qpos[3] = math.cos(half)
        self.data.qpos[4] = 0.0
        self.data.qpos[5] = 0.0
        self.data.qpos[6] = math.sin(half)
        self.data.qvel[0:6] = 0.0

    # ------------------------------------------------------------------ sensors
    def _pose(self):
        x, y = float(self.data.qpos[0]), float(self.data.qpos[1])
        w, z = float(self.data.qpos[3]), float(self.data.qpos[6])
        yaw = wrap_angle(2.0 * math.atan2(z, w))
        return x, y, yaw

    def _update_lidar(self):
        x, y, yaw = self._pose()
        scan_z = float(self.data.site_xpos[self.lidar_site][2])
        angles = np.linspace(-math.pi, math.pi, config.LIDAR_RAYS)
        points = []
        for angle in angles:
            a = yaw + angle
            self._ray_pnt[:] = (x, y, scan_z)
            self._ray_vec[:] = (
                config.LIDAR_RANGE * math.cos(a),
                config.LIDAR_RANGE * math.sin(a),
                0.0,
            )
            self._ray_geom[0] = -1
            distance = mujoco.mj_ray(
                self.model, self.data, self._ray_pnt, self._ray_vec,
                self.ray_filter, True, -1, self._ray_geom,
            )
            if self._ray_geom[0] >= 0 and distance < 1.0:
                px = x + self._ray_vec[0] * distance
                py = y + self._ray_vec[1] * distance
            else:
                px = x + self._ray_vec[0]
                py = y + self._ray_vec[1]
            points.append([round(px, 3), round(py, 3)])
        self.lidar_points = points
        self._last_lidar_time = time.time()

    def render_camera(self):
        with self.lock:
            now = time.time()
            if self._camera_bytes and now - self._camera_time < 1.0 / config.CAMERA_MAX_HZ:
                return self._camera_bytes
            if self._renderer is None:
                self._renderer = mujoco.Renderer(
                    self.model, config.CAMERA_HEIGHT, config.CAMERA_WIDTH
                )
                # 软件光栅化下阴影贴图极慢，关闭后单帧约 10 ms
                self._renderer.scene.flags[mujoco.mjtRndFlag.mjRND_SHADOW] = 0
            mujoco.mj_forward(self.model, self.data)
            self._renderer.update_scene(self.data, camera=self.camera_id)
            rgb = self._renderer.render()
            buffer = io.BytesIO()
            Image.fromarray(rgb).save(buffer, format="JPEG", quality=75)
            self._camera_bytes = buffer.getvalue()
            self._camera_time = now
            return self._camera_bytes

    # ------------------------------------------------------------------ control
    def _follow_path(self):
        x, y, yaw = self._pose()
        while self.path_index < len(self.path):
            tx, ty = self.path[self.path_index]
            distance = math.hypot(tx - x, ty - y)
            final = self.path_index == len(self.path) - 1
            if distance <= (config.FINAL_TOLERANCE if final else config.WAYPOINT_TOLERANCE):
                if final:
                    self.path_index = len(self.path)
                    self.navigating = False
                    self.arrived = True
                    return 0.0, 0.0
                self.path_index += 1
                continue
            heading = math.atan2(ty - y, tx - x)
            error = wrap_angle(heading - yaw)
            speed = min(config.MAX_LINEAR_SPEED, 0.9 * distance)
            if abs(error) > 0.55:
                speed = 0.10
            omega = max(-config.MAX_ANGULAR_SPEED, min(config.MAX_ANGULAR_SPEED, 2.2 * error))
            return speed, omega
        self.navigating = False
        return 0.0, 0.0

    def _apply_gait_targets(self):
        """按当前步态相位驱动髋/膝/踝与手臂电机。"""
        amp = self.gait_amp
        for side, offset in (("left", 0.0), ("right", math.pi)):
            s = math.sin(self.gait_phase + offset)
            hip = config.STEP_HIP * s * amp
            knee = config.STEP_KNEE * max(0.0, math.sin(self.gait_phase + offset + 0.6)) * amp
            ankle = max(-0.80, min(0.45, -(hip + knee) * 0.75))
            targets = {
                f"{side}_hip_pitch_joint": hip,
                f"{side}_knee_joint": knee,
                f"{side}_ankle_pitch_joint": ankle,
                f"{side}_shoulder_pitch_joint": 0.20 - config.STEP_ARM * s * amp,
                f"{side}_elbow_joint": 1.28 - 0.10 * max(0.0, s) * amp,
            }
            for name, angle in targets.items():
                index = self.actuators.get(name)
                if index is not None:
                    self.data.ctrl[index] = angle

    def _apply_motion(self, v, w, dt):
        self.cmd_v, self.cmd_w = v, w
        x, y, yaw = self._target_pose
        yaw = wrap_angle(yaw + w * dt)
        x += v * math.cos(yaw) * dt
        y += v * math.sin(yaw) * dt

        cell = self.grid.cell_size
        x = min(max(x, self.grid.min_x + 0.12), self.grid.min_x + self.grid.nx * cell - 0.12)
        y = min(max(y, self.grid.min_y + 0.12), self.grid.min_y + self.grid.ny * cell - 0.12)

        if abs(v) > 0.02:
            self.gait_phase += 2.0 * math.pi * v * dt / config.STEP_STRIDE
        elif abs(w) > 0.05:
            self.gait_phase += (1.0 if w > 0 else -1.0) * 0.9 * dt
        self.gait_phase %= 2.0 * math.pi

        target_amp = 1.0 if abs(v) > 0.03 else (0.45 if abs(w) > 0.1 else 0.0)
        self.gait_amp += (target_amp - self.gait_amp) * min(1.0, dt * 6.0)

        self._target_pose = (x, y, yaw)
        self._hold_base(x, y, yaw)
        self._apply_gait_targets()

    def _loop(self):
        dt = 1.0 / config.CONTROL_HZ
        while not self._stop:
            start = time.time()
            with self.lock:
                now = time.time()
                if now - self.teleop_time < 0.5:
                    v, w = self.teleop_v, self.teleop_w
                elif self.navigating:
                    v, w = self._follow_path()
                else:
                    v, w = 0.0, 0.0
                self._apply_motion(v, w, dt)
                for _ in range(config.SUBSTEPS):
                    mujoco.mj_step(self.model, self.data)
                x, y, yaw = self._target_pose
                self._hold_base(x, y, yaw)
                mujoco.mj_forward(self.model, self.data)
                if now - self._last_lidar_time > 0.2:
                    self._update_lidar()
                self._update_state()
            time.sleep(max(0.0, dt - (time.time() - start)))

    def _update_state(self):
        x, y, yaw = self._pose()
        z = float(self.data.qpos[2])
        joints = {
            name: round(float(self.data.qpos[adr]), 3)
            for name, adr in self.joint_qpos.items()
        }
        self._state = {
            "robot": {
                "x": round(x, 3),
                "y": round(y, 3),
                "z": round(z, 3),
                "yaw": round(yaw, 4),
                "v": round(abs(self.cmd_v), 3),
                "w": round(self.cmd_w, 3),
                "phase": round(self.gait_phase, 3),
                "joints": joints,
            },
            "path": [[round(px, 3), round(py, 3)] for px, py in self.path],
            "path_index": self.path_index,
            "navigating": self.navigating,
            "arrived": self.arrived,
            "lidar": self.lidar_points,
            "obstacles": self.obstacles,
        }

    # ------------------------------------------------------------------ API
    def state(self):
        with self.lock:
            state = dict(self._state)
            state["ok"] = True
            state["timestamp"] = round(time.time(), 3)
            return state

    def info(self):
        x, y, yaw = self._pose()
        return {
            "ok": True,
            "engine": "MuJoCo",
            "engine_version": mujoco.__version__,
            "physics_hz": config.PHYSICS_HZ,
            "control_hz": config.CONTROL_HZ,
            "robot": {
                "type": "unitree_g1_29dof",
                "model": "Unitree G1 (29-DoF, MuJoCo Menagerie)",
                "radius": config.ROBOT_RADIUS,
                "height": 1.32,
                "dof": len(self.actuators),
                "gait": {
                    "stride": config.STEP_STRIDE,
                    "max_speed": config.MAX_LINEAR_SPEED,
                },
                "sensors": ["lidar_2d", "head_rgb_camera", "imu(pose/velocity)"],
                "control": "29× position servo (kp=500, dampratio=1)",
            },
            "sensors": {
                "lidar": {
                    "rays": config.LIDAR_RAYS,
                    "range": config.LIDAR_RANGE,
                    "z": round(float(self.data.site_xpos[self.lidar_site][2]), 3),
                    "link": "lidar_site (mid360)",
                },
                "camera": {
                    "width": config.CAMERA_WIDTH,
                    "height": config.CAMERA_HEIGHT,
                    "fps": config.CAMERA_MAX_HZ,
                    "mount": "head_cam (d435)",
                    "height": round(float(self.data.cam_xpos[self.camera_id][2]), 3),
                    "pitch": config.CAMERA_PITCH,
                },
            },
            "scene": {
                "floor_offset": self.meta["floor_offset"],
                "gltf_bounds": self.meta["gltf_bounds"],
                "three_bounds": self.meta["three_bounds"],
                "bullet_bounds": self.meta["bullet_bounds"],
            },
            "spawn": list(self.spawn),
            "bounds": {
                "min_x": round(self.grid.min_x, 3),
                "min_y": round(self.grid.min_y, 3),
                "max_x": round(self.grid.min_x + self.grid.nx * self.grid.cell_size, 3),
                "max_y": round(self.grid.min_y + self.grid.ny * self.grid.cell_size, 3),
                "cell": self.grid.cell_size,
            },
        }

    def plan(self, goal_x, goal_y):
        with self.lock:
            if not (
                self.grid.min_x <= goal_x <= self.grid.min_x + self.grid.nx * self.grid.cell_size
                and self.grid.min_y <= goal_y <= self.grid.min_y + self.grid.ny * self.grid.cell_size
            ):
                return None, "目标点超出教室范围"
            if self.grid.is_blocked_world(goal_x, goal_y):
                return None, "目标点在障碍物内"
            x, y, _ = self._pose()
            path = self.grid.plan((x, y), (goal_x, goal_y))
            if not path:
                return None, "未找到可行路径"
            self.path = [[round(px, 3), round(py, 3)] for px, py in path]
            self.path_index = 0
            self.navigating = False
            self.arrived = False
            self._update_state()
            return self.path, None

    def start(self):
        with self.lock:
            if len(self.path) < 2:
                return False, "请先规划路径"
            self.path_index = 0
            self.navigating = True
            self.arrived = False
            self.teleop_time = 0.0
            self._update_state()
            return True, None

    def stop(self):
        with self.lock:
            self.navigating = False
            self.teleop_v = 0.0
            self.teleop_w = 0.0
            self.teleop_time = 0.0
            self._state["navigating"] = False
        return True

    def teleop(self, v, w):
        with self.lock:
            self.teleop_v = max(
                -config.MAX_LINEAR_SPEED, min(config.MAX_LINEAR_SPEED, float(v))
            )
            self.teleop_w = max(
                -config.MAX_ANGULAR_SPEED, min(config.MAX_ANGULAR_SPEED, float(w))
            )
            self.teleop_time = time.time()
            self.navigating = False
            self._state["navigating"] = False
        return True

    def reset(self):
        with self.lock:
            self.path = []
            self.path_index = 0
            self.navigating = False
            self.arrived = False
            self.teleop_time = 0.0
            self.teleop_v = 0.0
            self.teleop_w = 0.0
            self.cmd_v = 0.0
            self.cmd_w = 0.0
            self.gait_phase = 0.0
            self.gait_amp = 0.0
            self._camera_bytes = b""
            self._reset_pose()
        return True

    def add_obstacle(self, min_x, min_y, max_x, max_y, height=0.8):
        min_x, max_x = sorted((float(min_x), float(max_x)))
        min_y, max_y = sorted((float(min_y), float(max_y)))
        width, depth = max_x - min_x, max_y - min_y
        if width < 0.1 or depth < 0.1:
            return None, "障碍物太小"
        if width > 4.0 or depth > 4.0:
            return None, "障碍物太大"
        height = max(0.2, min(1.5, float(height)))
        with self.lock:
            if len(self.obstacles) >= MAX_OBSTACLES:
                return None, f"障碍物数量已达上限（{MAX_OBSTACLES}）"
            bounds = self.meta["bullet_bounds"]
            if (
                min_x < bounds[0][0] or max_x > bounds[1][0]
                or min_y < bounds[0][1] or max_y > bounds[1][1]
            ):
                return None, "障碍物超出教室范围"

            slot = len(self.obstacles)
            gid = self.obstacle_gids[slot]
            self.model.geom_size[gid] = [width / 2.0, depth / 2.0, height / 2.0]
            self.model.geom_pos[gid] = [
                (min_x + max_x) / 2.0, (min_y + max_y) / 2.0, height / 2.0,
            ]
            item = {
                "id": slot,
                "min_x": round(min_x, 3),
                "min_y": round(min_y, 3),
                "max_x": round(max_x, 3),
                "max_y": round(max_y, 3),
                "height": round(height, 3),
            }
            self.obstacles.append(item)
            self.navigating = False
            self.path = []
            self.path_index = 0
            self._rebuild_grid()
            self._update_state()
            return item, None

    def clear_obstacles(self):
        with self.lock:
            for gid in self.obstacle_gids:
                self.model.geom_pos[gid] = [0.0, 0.0, -50.0]
            self.obstacles = []
            self.navigating = False
            self.path = []
            self.path_index = 0
            self._rebuild_grid()
            self._update_state()
        return True
