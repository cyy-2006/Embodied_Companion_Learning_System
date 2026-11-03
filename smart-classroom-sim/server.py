"""智慧教室仿真服务（默认 MuJoCo，可用 SIM_ENGINE=pybullet 回退）。

启动：
    /root/.local/share/dsavd-mujoco-venv/bin/python server.py --host 127.0.0.1 --port 3100
"""
import argparse
import os

os.environ.setdefault("MUJOCO_GL", "osmesa")

from flask import Flask, Response, jsonify, request, send_from_directory

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

SIM_ENGINE = os.environ.get("SIM_ENGINE", "mujoco").strip().lower()
if SIM_ENGINE == "pybullet":
    from sim.world import ClassroomSim as SimClass
else:
    SIM_ENGINE = "mujoco"
    from sim.mjworld import MjClassroomSim as SimClass

app = Flask(__name__, static_folder=STATIC_DIR, static_url_path="")
sim = SimClass(BASE_DIR)


@app.after_request
def add_headers(response):
    if request.path.startswith("/api/"):
        response.headers["Cache-Control"] = "no-store"
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return response


@app.get("/")
def index():
    return send_from_directory(STATIC_DIR, "index.html")


@app.get("/api/sim/health")
def health():
    return jsonify({"ok": True, "engine": SIM_ENGINE})


@app.get("/api/sim/info")
def info():
    return jsonify(sim.info())


@app.get("/api/sim/state")
def state():
    return jsonify(sim.state())


@app.post("/api/sim/plan")
def plan():
    data = request.get_json(silent=True) or {}
    try:
        x = float(data["x"])
        y = float(data["y"])
    except (KeyError, TypeError, ValueError):
        return jsonify({"ok": False, "error": "需要数值 x/y（PyBullet 世界坐标）"}), 400
    path, error = sim.plan(x, y)
    if error:
        return jsonify({"ok": False, "error": error}), 400
    return jsonify({"ok": True, "path": path})


@app.post("/api/sim/start")
def start():
    ok, error = sim.start()
    return jsonify({"ok": ok, "error": error}), (200 if ok else 400)


@app.post("/api/sim/stop")
def stop():
    sim.stop()
    return jsonify({"ok": True})


@app.post("/api/sim/reset")
def reset():
    sim.reset()
    return jsonify({"ok": True})


@app.post("/api/sim/teleop")
def teleop():
    data = request.get_json(silent=True) or {}
    try:
        v = float(data.get("v", 0.0))
        w = float(data.get("w", 0.0))
    except (TypeError, ValueError):
        return jsonify({"ok": False, "error": "v/w 必须是数值"}), 400
    sim.teleop(v, w)
    return jsonify({"ok": True})


@app.post("/api/sim/obstacle")
def add_obstacle():
    data = request.get_json(silent=True) or {}
    try:
        item, error = sim.add_obstacle(
            data["min_x"], data["min_y"], data["max_x"], data["max_y"],
            data.get("height", 0.8),
        )
    except (KeyError, TypeError, ValueError):
        return jsonify({"ok": False, "error": "需要 min_x/min_y/max_x/max_y"}), 400
    if error:
        return jsonify({"ok": False, "error": error}), 400
    return jsonify({"ok": True, "obstacle": item})


@app.post("/api/sim/obstacles/clear")
def clear_obstacles():
    sim.clear_obstacles()
    return jsonify({"ok": True})


@app.get("/api/sim/camera.jpg")
def camera():
    image = sim.render_camera()
    return Response(image, mimetype="image/jpeg")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=3100)
    args = parser.parse_args()
    app.run(host=args.host, port=args.port, threaded=True, use_reloader=False)
