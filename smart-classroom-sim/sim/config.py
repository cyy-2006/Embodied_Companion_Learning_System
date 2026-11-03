"""仿真参数（单位：米 / 秒 / 弧度）。"""

# 栅格与机器人
CELL_SIZE = 0.15
ROBOT_RADIUS = 0.24
GRID_MARGIN = 0.30
INFLATE_RADIUS = 0.24

# 宇树 G1 29-DoF 人形
HUMANOID_BASE_Z = 0.79      # 骨盆中心离地高度（官方 stand 关键帧）
MAX_LINEAR_SPEED = 0.6
MAX_ANGULAR_SPEED = 1.2
STEP_STRIDE = 0.50          # 一个完整步态周期（左右各一步）前进的距离
STEP_HIP = 0.30             # 髋关节摆幅
STEP_KNEE = 0.45            # 摆动腿膝关节弯曲峰值
STEP_ARM = 0.24             # 手臂反向摆幅
STEP_BOB = 0.010            # 骨盆上下起伏

# 时间步
PHYSICS_HZ = 240
CONTROL_HZ = 30
SUBSTEPS = PHYSICS_HZ // CONTROL_HZ

# 传感器
LIDAR_RAYS = 181
LIDAR_RANGE = 6.0
LIDAR_Z = 1.17              # mid360 雷达安装高度（实际按 link 位姿动态取值）
CAMERA_WIDTH = 320
CAMERA_HEIGHT = 240
CAMERA_FOV = 65.0
CAMERA_PITCH = -0.14        # 头部相机俯仰角（向下为负）
CAMERA_MAX_HZ = 1.0
CAMERA_LINK = "d435_link"   # 头部 RealSense D435 传感器坐标系
LIDAR_LINK = "mid360_link"  # 头部 Livox Mid-360 雷达坐标系

# 规划
WAYPOINT_TOLERANCE = 0.16
FINAL_TOLERANCE = 0.10
