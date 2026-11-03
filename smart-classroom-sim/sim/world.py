"""PyBullet 智慧教室仿真世界。

坐标系：
- PyBullet 世界：X 向前/向右，Y 向左，Z 向上，地面 z=0。
- 原 GLTF：Y-up，Z 为教室长轴。
- 浏览器 Three.js：Y-up，使用与 PyBullet 的映射 (x, z, -y)。
"""
import io
import json
import math
import os
import threading
import time
from collections import deque

import numpy as np
import pybullet as p
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


class ClassroomSim:
    def __init__(self, base_dir):
        self.base_dir = os.path.abspath(base_dir)
        self.assets_dir = os.path.join(self.base_dir, "assets")
        self.lock = threading.RLock()
        self.client = p.connect(p.DIRECT)
        p.setGravity(0, 0, -9.81, physicsClientId=self.client)
        p.setTimeStep(1.0 / config.PHYSICS_HZ, physicsClientId=self.client)
        p.setPhysicsEngineParameter(
            numSolverIterations=24,
            numSubSteps=1,
            physicsClientId=self.client,
        )

        with open(os.path.join(self.assets_dir, "scene_meta.json"), "r", encoding="utf-8") as f:
            self.meta = json.load(f)

        self.scene_id = None
        self.floor_id = None
        self.robot_id = None
        self.joints = {}
        self.gait_phase = 0.0
        self.gait_amp = 0.0
        self.cmd_v = 0.0
        self.cmd_w = 0.0
        self.obstacle_ids = []
        self.obstacles = []
        self.grid = None
        self.spawn = (1.4, 0.0, 0.0)
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
        self._state = {}
        self._stop = False
        self._thread = None

        with self.lock:
            self._load_world()

        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()

    # ------------------------------------------------------------------ setup
    def _load_world(self):
        obj_path = os.path.join(self.assets_dir, "classroom.obj")
        self.scene_id = self._create_mesh_body(obj_path)

        # 地面法线在下，射线会被背面剔除；额外加一层不可见地面保证机器人有支撑
        floor_col = p.createCollisionShape(
            p.GEOM_PLANE, planeNormal=[0, 0, 1], physicsClientId=self.client
        )
        self.floor_id = p.createMultiBody(
            0, floor_col, -1, [0, 0, 0], physicsClientId=self.client
        )
        p.changeDynamics(
            self.floor_id, -1, lateralFriction=1.0, restitution=0.0,
            physicsClientId=self.client,
        )

        self._build_grid()
        spawn = self._find_spawn()
        self.spawn = (spawn[0], spawn[1], config.HUMANOID_BASE_Z)
        self._spawn_robot()

    def _create_mesh_body(self, obj_path):
        col = p.createCollisionShape(
            p.GEOM_MESH,
            fileName=obj_path,
            flags=p.GEOM_FORCE_CONCAVE_TRIMESH,
            physicsClientId=self.client,
        )
        vis = p.createVisualShape(
            p.GEOM_MESH, fileName=obj_path, physicsClientId=self.client
        )
        body = p.createMultiBody(
            0, col, vis, [0, 0, 0], physicsClientId=self.client
        )
        p.changeDynamics(
            body, -1, lateralFriction=1.0, restitution=0.0,
            physicsClientId=self.client,
        )
        tex_path = os.path.join(self.assets_dir, "material_0.png")
        if os.path.exists(tex_path):
            try:
                tex = p.loadTexture(tex_path, physicsClientId=self.client)
                p.changeVisualShape(
                    body, -1, textureUniqueId=tex, physicsClientId=self.client
                )
            except Exception:
                pass
        return body

    def _build_grid(self):
        bounds = self.meta["bullet_bounds"]
        min_x = bounds[0][0] + config.GRID_MARGIN
        min_y = bounds[0][1] + config.GRID_MARGIN
        max_x = bounds[1][0] - config.GRID_MARGIN
        max_y = bounds[1][1] - config.GRID_MARGIN
        nx = int(math.ceil((max_x - min_x) / config.CELL_SIZE))
        ny = int(math.ceil((max_y - min_y) / config.CELL_SIZE))
        xs = min_x + (np.arange(nx) + 0.5) * config.CELL_SIZE
        ys = min_y + (np.arange(ny) + 0.5) * config.CELL_SIZE
        centers = [(x, y) for x in xs for y in ys]

        starts = [[x, y, 1.80] for x, y in centers]
        ends = [[x, y, 0.02] for x, y in centers]
        hits = p.rayTestBatch(
            starts, ends, numThreads=2, physicsClientId=self.client
        )

        blocked = np.zeros(nx * ny, dtype=bool)
        occupied_ids = {self.scene_id, self.floor_id}
        occupied_ids.update(self.obstacle_ids)
        if self.robot_id is not None:
            occupied_ids.discard(self.robot_id)

        for idx, hit in enumerate(hits):
            if idx >= nx * ny:
                break
            obj_id, _, _, hit_pos, _ = hit
            if obj_id in occupied_ids and hit_pos[2] > 0.10:
                blocked[idx] = True
            elif obj_id not in (-1, self.floor_id, self.scene_id) and obj_id != self.robot_id:
                # 其他障碍物（例如之后添加的盒体）
                blocked[idx] = True

        blocked = blocked.reshape((nx, ny))

        # 四周留出一格安全边界
        blocked[0, :] = True
        blocked[-1, :] = True
        blocked[:, 0] = True
        blocked[:, -1] = True

        blocked = self._inflate(blocked, int(math.ceil(config.INFLATE_RADIUS / config.CELL_SIZE)))
        self.grid = GridMap(blocked, min_x, min_y, config.CELL_SIZE)

    def _inflate(self, blocked, radius_cells):
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

    def _spawn_robot(self):
        urdf = os.path.join(
            self.base_dir, "static", "assets", "g1", "g1_29dof.urdf"
        )
        x, y, z = self.spawn
        self.robot_id = p.loadURDF(
            urdf,
            basePosition=[x, y, z],
            baseOrientation=p.getQuaternionFromEuler([0, 0, 0]),
            useFixedBase=False,
            flags=p.URDF_USE_INERTIA_FROM_FILE,
            physicsClientId=self.client,
        )
        self.joints = {}
        self._link_ids = {}
        for j in range(p.getNumJoints(self.robot_id, physicsClientId=self.client)):
            info = p.getJointInfo(self.robot_id, j, physicsClientId=self.client)
            name = info[1].decode("utf-8")
            self._link_ids[info[12].decode("utf-8")] = j
            if info[2] != p.JOINT_REVOLUTE:
                continue
            self.joints[name] = j
            p.setJointMotorControl2(
                self.robot_id, j, p.POSITION_CONTROL, targetPosition=0.0,
                force=self._joint_force(name), positionGain=0.55,
                velocityGain=0.45, physicsClientId=self.client,
            )
            p.changeDynamics(
                self.robot_id, j, lateralFriction=1.2,
                jointDamping=0.04, physicsClientId=self.client,
            )
        p.changeDynamics(
            self.robot_id, -1, lateralFriction=1.0, restitution=0.0,
            physicsClientId=self.client,
        )
        self._target_pose = (x, y, 0.0)
        self._apply_stand_pose()
        p.resetBaseVelocity(
            self.robot_id, [0, 0, 0], [0, 0, 0], physicsClientId=self.client
        )
        self._update_lidar()

    def _apply_stand_pose(self):
        for name, joint in self.joints.items():
            p.setJointMotorControl2(
                self.robot_id, joint, p.POSITION_CONTROL,
                targetPosition=STAND_POSE.get(name, 0.0),
                force=self._joint_force(name), positionGain=0.55,
                velocityGain=0.45, physicsClientId=self.client,
            )

    def _link_position(self, name):
        index = getattr(self, "_link_ids", {}).get(name)
        if index is None:
            return None
        return p.getLinkState(
            self.robot_id, index, computeForwardKinematics=1,
            physicsClientId=self.client,
        )[0]

    @staticmethod
    def _joint_force(name):
        if "knee" in name:
            return 55.0
        if "hip" in name:
            return 45.0
        if "ankle" in name:
            return 30.0
        if "waist" in name:
            return 25.0
        if "elbow" in name:
            return 20.0
        if "shoulder" in name:
            return 12.0
        return 10.0

    # ------------------------------------------------------------------ sensors
    def _base_pose(self):
        pos, orn = p.getBasePositionAndOrientation(
            self.robot_id, physicsClientId=self.client
        )
        euler = p.getEulerFromQuaternion(orn)
        return pos, orn, euler

    def _update_lidar(self):
        pos, _, euler = self._base_pose()
        yaw = euler[2]
        link = self._link_position(config.LIDAR_LINK)
        scan_z = link[2] if link else config.LIDAR_Z
        angles = np.linspace(-math.pi, math.pi, config.LIDAR_RAYS)
        starts = []
        ends = []
        for angle in angles:
            a = yaw + angle
            starts.append([pos[0], pos[1], scan_z])
            ends.append([
                pos[0] + config.LIDAR_RANGE * math.cos(a),
                pos[1] + config.LIDAR_RANGE * math.sin(a),
                scan_z,
            ])
        hits = p.rayTestBatch(
            starts, ends, numThreads=2, physicsClientId=self.client
        )
        points = []
        for idx, hit in enumerate(hits):
            obj_id, _, fraction, hit_pos, _ = hit
            if obj_id == self.robot_id:
                continue
            if fraction < 1.0:
                points.append([round(hit_pos[0], 3), round(hit_pos[1], 3)])
            else:
                # 未命中时给出量程端点，前端据此画出扫描边界
                endpoint = ends[idx]
                points.append([round(endpoint[0], 3), round(endpoint[1], 3)])
        self.lidar_points = points
        self._last_lidar_time = time.time()

    def render_camera(self):
        with self.lock:
            now = time.time()
            if self._camera_bytes and now - self._camera_time < 1.0 / config.CAMERA_MAX_HZ:
                return self._camera_bytes

            pos, _, euler = self._base_pose()
            yaw = euler[2]
            fx, fy = math.cos(yaw), math.sin(yaw)
            # 头部 RealSense D435：直接取 URDF 中 d435_link 的世界位姿
            link = self._link_position(config.CAMERA_LINK)
            if link:
                eye = [link[0], link[1], link[2]]
            else:
                eye = [pos[0], pos[1], pos[2] + 1.25]
            cos_p = math.cos(config.CAMERA_PITCH)
            sin_p = math.sin(config.CAMERA_PITCH)
            target = [
                eye[0] + 2.0 * fx * cos_p,
                eye[1] + 2.0 * fy * cos_p,
                eye[2] + 2.0 * sin_p,
            ]
            view = p.computeViewMatrix(eye, target, [0, 0, 1])
            proj = p.computeProjectionMatrixFOV(
                config.CAMERA_FOV,
                config.CAMERA_WIDTH / config.CAMERA_HEIGHT,
                0.05,
                30.0,
            )
            image = p.getCameraImage(
                config.CAMERA_WIDTH,
                config.CAMERA_HEIGHT,
                view,
                proj,
                renderer=p.ER_TINY_RENDERER,
                physicsClientId=self.client,
            )
            rgba = np.asarray(image[2])
            if rgba.ndim == 1:
                rgba = rgba.reshape(config.CAMERA_HEIGHT, config.CAMERA_WIDTH, 4)
            # ER_TINY_RENDERER 返回的数组已是左上角为原点，不能再做上下翻转
            rgb = rgba[:, :, :3].astype(np.uint8)
            buffer = io.BytesIO()
            Image.fromarray(rgb).save(buffer, format="JPEG", quality=75)
            self._camera_bytes = buffer.getvalue()
            self._camera_time = now
            return self._camera_bytes

    # ------------------------------------------------------------------ control
    def _follow_path(self):
        pos, _, euler = self._base_pose()
        x, y = pos[0], pos[1]
        yaw = euler[2]
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
        """按当前步态相位驱动髋/膝/踝与手臂关节。"""
        amp = self.gait_amp
        for side, offset in (("left", 0.0), ("right", math.pi)):
            s = math.sin(self.gait_phase + offset)
            hip = config.STEP_HIP * s * amp
            knee = config.STEP_KNEE * max(0.0, math.sin(self.gait_phase + offset + 0.6)) * amp
            ankle = -(hip + knee) * 0.75
            ankle = max(-0.80, min(0.45, ankle))
            targets = {
                f"{side}_hip_pitch_joint": hip,
                f"{side}_knee_joint": knee,
                f"{side}_ankle_pitch_joint": ankle,
                f"{side}_shoulder_pitch_joint": 0.20 - config.STEP_ARM * s * amp,
                f"{side}_elbow_joint": 1.28 - 0.10 * max(0.0, s) * amp,
            }
            for name, angle in targets.items():
                joint = self.joints.get(name)
                if joint is None:
                    continue
                p.setJointMotorControl2(
                    self.robot_id, joint, p.POSITION_CONTROL,
                    targetPosition=angle, force=self._joint_force(name),
                    positionGain=0.55, velocityGain=0.45,
                    physicsClientId=self.client,
                )

    def _apply_motion(self, v, w, dt):
        """双足步态：按指令速度推进基座位姿，并更新步态相位。"""
        self.cmd_v, self.cmd_w = v, w
        pos, _, euler = self._base_pose()
        yaw = euler[2] + w * dt
        yaw = (yaw + math.pi) % (2.0 * math.pi) - math.pi
        x = pos[0] + v * math.cos(yaw) * dt
        y = pos[1] + v * math.sin(yaw) * dt

        # 限制在可行栅格内，避免手动驾驶穿墙
        cell = self.grid.cell_size
        x = min(max(x, self.grid.min_x + 0.12), self.grid.min_x + self.grid.nx * cell - 0.12)
        y = min(max(y, self.grid.min_y + 0.12), self.grid.min_y + self.grid.ny * cell - 0.12)

        if abs(v) > 0.02:
            self.gait_phase += 2.0 * math.pi * v * dt / config.STEP_STRIDE
        elif abs(w) > 0.05:
            self.gait_phase += (1.0 if w > 0 else -1.0) * 0.9 * dt
        self.gait_phase %= 2.0 * math.pi

        # 静止时收敛到直立站姿，起步/停车时平滑过渡
        target_amp = 1.0 if abs(v) > 0.03 else (0.45 if abs(w) > 0.1 else 0.0)
        self.gait_amp += (target_amp - self.gait_amp) * min(1.0, dt * 6.0)

        self._target_pose = (x, y, yaw)
        self._hold_base(x, y, yaw)
        self._apply_gait_targets()

    def _hold_base(self, x, y, yaw):
        z = config.HUMANOID_BASE_Z + config.STEP_BOB * abs(math.sin(self.gait_phase))
        p.resetBasePositionAndOrientation(
            self.robot_id, [x, y, z],
            p.getQuaternionFromEuler([0, 0, yaw]),
            physicsClientId=self.client,
        )
        p.resetBaseVelocity(
            self.robot_id, [0, 0, 0], [0, 0, 0],
            physicsClientId=self.client,
        )

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
                    p.stepSimulation(physicsClientId=self.client)
                # 物理步进后把根节点拉回指令位姿，保证双足直立不跌倒
                x, y, yaw = self._target_pose
                self._hold_base(x, y, yaw)
                if now - self._last_lidar_time > 0.2:
                    self._update_lidar()
                self._update_state()
            elapsed = time.time() - start
            time.sleep(max(0.0, dt - elapsed))

    def _update_state(self):
        pos, _, euler = self._base_pose()
        joints = {}
        for name, joint in self.joints.items():
            joints[name] = round(
                p.getJointState(self.robot_id, joint, physicsClientId=self.client)[0], 3
            )
        self._state = {
            "robot": {
                "x": round(pos[0], 3),
                "y": round(pos[1], 3),
                "z": round(pos[2], 3),
                "yaw": round(euler[2], 4),
                "v": round(abs(self.cmd_v), 3),
                "w": round(self.cmd_w, 3),
                "phase": round(self.gait_phase, 3),
                "joints": joints,
            },
            "path": [[round(x, 3), round(y, 3)] for x, y in self.path],
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
        lidar = self._link_position(config.LIDAR_LINK)
        camera = self._link_position(config.CAMERA_LINK)
        return {
            "ok": True,
            "engine": "PyBullet",
            "physics_hz": config.PHYSICS_HZ,
            "control_hz": config.CONTROL_HZ,
            "robot": {
                "type": "unitree_g1_29dof",
                "model": "Unitree G1 (29-DoF)",
                "radius": config.ROBOT_RADIUS,
                "height": 1.32,
                "dof": len(self.joints),
                "gait": {
                    "stride": config.STEP_STRIDE,
                    "max_speed": config.MAX_LINEAR_SPEED,
                },
                "sensors": ["lidar_2d", "head_rgb_camera", "imu(pose/velocity)"],
            },
            "sensors": {
                "lidar": {
                    "rays": config.LIDAR_RAYS,
                    "range": config.LIDAR_RANGE,
                    "z": round(lidar[2], 3) if lidar else config.LIDAR_Z,
                    "link": config.LIDAR_LINK,
                },
                "camera": {
                    "width": config.CAMERA_WIDTH,
                    "height": config.CAMERA_HEIGHT,
                    "fps": config.CAMERA_MAX_HZ,
                    "mount": config.CAMERA_LINK,
                    "height": round(camera[2], 3) if camera else None,
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
            pos, _, _ = self._base_pose()
            path = self.grid.plan((pos[0], pos[1]), (goal_x, goal_y))
            if not path:
                return None, "未找到可行路径"
            self.path = [[round(x, 3), round(y, 3)] for x, y in path]
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
            self._target_pose = (self.spawn[0], self.spawn[1], 0.0)
            p.resetBasePositionAndOrientation(
                self.robot_id,
                [self.spawn[0], self.spawn[1], config.HUMANOID_BASE_Z],
                p.getQuaternionFromEuler([0, 0, 0]),
                physicsClientId=self.client,
            )
            p.resetBaseVelocity(
                self.robot_id, [0, 0, 0], [0, 0, 0],
                physicsClientId=self.client,
            )
            self._apply_stand_pose()
            self._update_lidar()
            self._update_state()
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
            bounds = self.meta["bullet_bounds"]
            if (
                min_x < bounds[0][0] or max_x > bounds[1][0]
                or min_y < bounds[0][1] or max_y > bounds[1][1]
            ):
                return None, "障碍物超出教室范围"
            col = p.createCollisionShape(
                p.GEOM_BOX,
                halfExtents=[width / 2.0, depth / 2.0, height / 2.0],
                physicsClientId=self.client,
            )
            vis = p.createVisualShape(
                p.GEOM_BOX,
                halfExtents=[width / 2.0, depth / 2.0, height / 2.0],
                rgbaColor=[0.95, 0.55, 0.12, 0.65],
                physicsClientId=self.client,
            )
            body = p.createMultiBody(
                0, col, vis,
                [(min_x + max_x) / 2.0, (min_y + max_y) / 2.0, height / 2.0],
                physicsClientId=self.client,
            )
            self.obstacle_ids.append(body)
            item = {
                "id": body,
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
            self._build_grid()
            self._update_state()
            return item, None

    def clear_obstacles(self):
        with self.lock:
            for body in self.obstacle_ids:
                p.removeBody(body, physicsClientId=self.client)
            self.obstacle_ids = []
            self.obstacles = []
            self.navigating = False
            self.path = []
            self.path_index = 0
            self._build_grid()
            self._update_state()
        return True
