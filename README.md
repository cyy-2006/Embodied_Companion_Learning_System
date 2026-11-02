# Embodied Companion Learning System（智慧学习 / 智慧教室平台）

一套面向课堂行为分析与具身智能教学的一体化平台：Vue 前端 + Flask 后端 + 独立的 PyBullet 人形机器人仿真服务，覆盖课堂视频、行为识别、表情/姿态分析、考试监考、巡课（RSM）与 3D 智慧教室仿真。

## 目录结构

```
.
├── App/                      Flask 后端主服务（AI 能力 + 业务接口）
│   ├── app.py                主应用与全部 HTTP 路由
│   ├── voice_recognition/    语音识别（faster-whisper）
│   ├── face_emotion/         表情识别（deepface + 本地权重）
│   ├── pose_detection/       人体姿态检测（YOLOv8-pose）
│   ├── camera_yolo.py        摄像头实时检测
│   ├── templates/            视频页面模板
│   ├── sqlite3db/            建表脚本（sqlite / mysql）
│   ├── fonts/ report/ uploads/ result/ dsvideo/   运行时目录
│   └── requirements-deploy.txt / requirements-ai.txt
├── frontend/dist/            前端构建产物（Vue2 + ECharts + Three.js）
│   ├── index.html
│   ├── smart-classroom-sim/  智慧教室人形仿真页面（内嵌副本）
│   └── japanese-classroom/   教室三维场景资源
├── smart-classroom-sim/      PyBullet 人形机器人仿真（独立进程）
│   ├── server.py             Flask 仿真 API（默认 127.0.0.1:3100）
│   ├── sim/world.py          物理世界、人形步态、雷达、头部相机
│   ├── sim/planner.py        二维栅格 A* 规划与路径平滑
│   ├── sim/config.py         仿真参数
│   ├── assets/               教室 OBJ、贴图、场景元数据、robot.urdf（双足人形）
│   ├── static/               仿真页面（Three.js 渲染 + 控制面板）
│   └── tools/convert_scene.py GLTF → OBJ 转换脚本
├── deploy/                   生产部署配置
│   ├── nginx/dsavd.conf      nginx 站点配置（含旧 3D 教室页重定向）
│   └── systemd/              主服务与仿真服务 unit
├── config.yaml               服务端口、MySQL、DeepTutor 集成配置
└── LICENSE
```

## 本次更新（2026-11-02）

### 1. 智慧教室仿真改造为「双足人形 + 头部相机」

原先的脚本化 3D 教室已替换为基于 PyBullet 的具身仿真：

- **机器人模型**：`smart-classroom-sim/assets/robot.urdf` 由差速底盘重写为双足人形——骨盆、躯干、头部、双臂（肩/肘）、双腿（髋/膝/踝），共 10 个 revolute 关节，机体高 1.48 m。
- **运动方式**：运动学基座保持直立 + 关节位置控制（`POSITION_CONTROL`）的程序化步态。步态相位由行进距离推进，髋摆动、膝屈曲、踝补偿、手臂反摆，静止时振幅平滑收敛为直立站姿，避免双足动力学失衡跌倒。
- **头部摄像头**：安装在头前方 0.13 m、眼高约 1.38 m，固定下俯角 65° FOV，320×240 渲染，1 Hz 缓存，输出 JPEG。
- **2D 雷达**：181 束射线、量程 6 m，随位姿实时更新。
- **导航**：0.15 m 栅格 + 膨胀半径 0.24 m 的二维 A*（8 邻域、防切角、视线平滑），支持点击地面规划、路径跟踪、手动遥操作与动态障碍物。
- **修复**：`ER_TINY_RENDERER` 返回的像素数组本身已是左上原点，原先多余的 `[::-1]` 会让画面上下翻转，现已移除（`sim/world.py`）。

### 2. 接入主服务器项目，替换原教室接口

- `App/app.py` 删除旧的脚本教室接口：
  - `GET  /rsm/classroom/route/list`
  - `POST /rsm/classroom/route`
  - `DELETE /rsm/classroom/route/<int:route_id>`
- 新增转发到独立仿真进程的代理接口（`CLASSROOM_SIM_URL`，默认 `http://127.0.0.1:3100/api/sim`）：
  `health`、`info`、`state`、`plan`、`start`、`stop`、`reset`、`teleop`、`obstacle`、`obstacles/clear`、`camera.jpg`，统一前缀 `/api/rsm/classroom/sim/`。
- nginx 将旧页面地址 `/smart-classroom/3d` 302 到新页面 `/smart-classroom-sim/`。
- 仿真服务由 systemd 常驻（`dsavd-classroom-sim.service`），主站 gunicorn 不承担仿真计算，重启互不影响。

## 系统架构

```
浏览器
  └─ nginx :80
       ├─ /                     → frontend/dist（Vue 静态页）
       ├─ /api/*                → 127.0.0.1:3000（gunicorn + App/app.py）
       │                            └─ /api/rsm/classroom/sim/* → 127.0.0.1:3100（PyBullet 仿真）
       ├─ /smart-classroom-sim/ → frontend/dist/smart-classroom-sim（仿真页面）
       └─ /smart-classroom/3d   → 302 重定向到 /smart-classroom-sim/
```

仿真进程内部：PyBullet `DIRECT` 模式（无窗口）+ 后台线程以 240 Hz 物理步进 / 30 Hz 控制，Flask 仅暴露 HTTP API 与 JPEG 图像。

## 运行与部署

### 后端主服务

```bash
python3 -m venv /opt/dsavd-venv
/opt/dsavd-venv/bin/pip install -r App/requirements-deploy.txt
# AI 相关能力（可选，体积较大）
/opt/dsavd-venv/bin/pip install -r App/requirements-ai.txt

# 依赖 Redis（app.py 启动即连接 localhost:6379）
/opt/dsavd-venv/bin/gunicorn --bind 127.0.0.1:3000 --workers 1 --threads 4 --timeout 900 app:app
```

环境变量（生产用 `EnvironmentFile`）：

| 变量 | 用途 |
| --- | --- |
| `DSAVD_SECRET_KEY` | Flask session 密钥 |
| `DSAVD_MYSQL_PASSWORD` | MySQL 密码（未设置时取 `config.yaml`） |
| `DEEPTUTOR_ROOT` | DeepTutor 安装目录 |
| `CLASSROOM_SIM_URL` | 仿真服务地址，默认 `http://127.0.0.1:3100/api/sim` |

### 仿真服务

```bash
python3 -m venv /root/.local/share/dsavd-sim-venv
/root/.local/share/dsavd-sim-venv/bin/pip install -r smart-classroom-sim/requirements.txt
cd smart-classroom-sim && ./run.sh --host 127.0.0.1 --port 3100
```

`run.sh` 依次尝试 `$PYTHON`、`/root/.local/share/dsavd-sim-venv/bin/python`、`python3`。首次加载教室网格约需 10 s。

### systemd / nginx

```bash
cp deploy/systemd/*.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable --now dsavd.service dsavd-classroom-sim.service

cp deploy/nginx/dsavd.conf /etc/nginx/conf.d/dsavd.conf
nginx -t && systemctl reload nginx
```

### 数据库

```bash
python3 App/sqlite3db/init_shared_mysql.py     # MySQL 版
# 或按需执行同目录下的建表脚本（sqlite 版为 dsavd.db）
```

## 仿真 HTTP API

| 方法 | 路径（仿真进程内为 `/api/sim/*`，主站为 `/api/rsm/classroom/sim/*`） | 说明 |
| --- | --- | --- |
| GET | `/health` | 存活检查 |
| GET | `/info` | 引擎、机器人类型、传感器、场景边界 |
| GET | `/state` | 位姿、速度、步态相位、10 个关节角、雷达点、路径 |
| POST | `/plan` | `{"x":..,"y":..}` 规划路径 |
| POST | `/start` / `/stop` | 开始 / 停止导航 |
| POST | `/reset` | 机器人复位到出生点 |
| POST | `/teleop` | `{"v":..,"w":..}` 速度指令 |
| POST | `/obstacle` | `{"min_x","min_y","max_x","max_y","height"}` 添加障碍 |
| POST | `/obstacles/clear` | 清空动态障碍 |
| GET | `/camera.jpg` | 头部相机 JPEG（320×240） |

## 仿真页面使用

1. 打开 `/smart-classroom-sim/`，等待模型加载（机器人初始隐藏，收到首帧状态后显示）。
2. 点击地面 → 规划路径（成功提示「已规划 N 个路径点」）→ 点「开始导航」。
3. `WASD` 遥操作双足行走，`Q/E` 原地转向。
4. 勾选「显示相机画面」拉取头部摄像头实时图像；雷达点云随位姿刷新。
5. 「放置障碍」可在场景中插入盒体并重算栅格。

## 未纳入版本库的文件

| 内容 | 原因 |
| --- | --- |
| `App/dsvideo/**/*.mp4`、`App/templates/*.mp4`、`frontend/dist/media/*.mp4` | 课程视频体积过大（合计 4 GB+），按需求不推送 |
| `App/yolov8x-pose-p6.pt` | 190 MB，超过 GitHub 单文件 100 MB 限制；缺失时由 ultralytics 自动下载 |
| `App/sqlite3db/*.db` | 本地运行时数据库，可用同目录脚本重建 |
| `App/report/*.pdf`、`App/uploads/*`、`App/result/*` | 运行时生成的学生报告与上传文件 |
| `__pycache__`、`*.pyc`、`*.bak.*`、日志 | 构建与备份产物 |

## 已知限制

- 前端 `dist` 为构建产物，Vue 源码不在本仓库，无法直接改菜单与路由。
- 双足为运动学基座 + 关节动画的混合方案，不具备完整动力学平衡控制；如需真实双足，可替换为基于 `TORQUE_CONTROL` 的步态控制器。
- 仿真依赖 CPU 渲染（`ER_TINY_RENDERER`），高并发下相机帧率受限（默认 1 Hz）。
