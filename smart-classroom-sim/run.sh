#!/usr/bin/env bash
# 启动智慧教室 PyBullet 仿真服务
set -euo pipefail

cd "$(dirname "$0")"

VENV_PY=/root/.local/share/dsavd-sim-venv/bin/python
if [ -n "${PYTHON:-}" ]; then
  exec "$PYTHON" server.py "$@"
elif [ -x "$VENV_PY" ]; then
  exec "$VENV_PY" server.py "$@"
else
  exec python3 server.py "$@"
fi
