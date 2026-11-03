import * as THREE from 'three';
import { OrbitControls } from './vendor/jsm/controls/OrbitControls.js';
import { GLTFLoader } from './vendor/jsm/loaders/GLTFLoader.js';
import { loadURDF } from './urdf-loader.js?v=20261103';

// 独立运行时走 Flask 的相对接口；部署到主站 /smart-classroom-sim/ 时走主服务代理接口
const IN_SERVER = location.pathname.startsWith('/smart-classroom-sim');
const API_BASE = IN_SERVER ? '/api/rsm/classroom/sim' : './api/sim';
const ASSET_BASE = IN_SERVER ? '/smart-classroom-sim/assets' : './assets';

const canvas = document.getElementById('view');
const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.outputColorSpace = THREE.SRGBColorSpace;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.0;

const scene = new THREE.Scene();
scene.background = new THREE.Color(0x0b1220);
scene.fog = new THREE.Fog(0x0b1220, 26, 55);

const camera = new THREE.PerspectiveCamera(
  50, window.innerWidth / window.innerHeight, 0.1, 120
);

const controls = new OrbitControls(camera, canvas);
controls.enableDamping = true;
controls.dampingFactor = 0.08;
controls.minDistance = 2;
controls.maxDistance = 45;
controls.maxPolarAngle = Math.PI / 2 - 0.04;

scene.add(new THREE.HemisphereLight(0xdce9ff, 0x18202e, 1.15));
const sun = new THREE.DirectionalLight(0xffffff, 1.4);
sun.position.set(6, 12, 4);
scene.add(sun);
const fill = new THREE.DirectionalLight(0x9fb8ff, 0.45);
fill.position.set(-6, 6, -5);
scene.add(fill);

// ------------------------------------------------------------------ world
let info = null;
let model = null;
let floorPlane = null;
let bounds = null;
let lidarHeight = 1.17;

// ------------------------------------------------------------------ robot
const robotGroup = new THREE.Group();
scene.add(robotGroup);

const robotJoints = {};
let robotReady = false;

// 加载宇树 G1 官方 URDF（Z-up），旋转后挂到 Y-up 场景里
async function buildRobot() {
  const { root, joints } = await loadURDF(`${ASSET_BASE}/g1/g1_29dof.urdf`);
  root.rotation.x = -Math.PI / 2;
  robotGroup.add(root);
  for (const [name, joint] of Object.entries(joints)) robotJoints[name] = joint;
  robotReady = true;
  window.__g1Ready = true;
  console.info(`G1 模型已加载：${Object.keys(robotJoints).length} 个关节`);
}
robotGroup.visible = false;

// 关节绕 URDF 自身轴向旋转，角度直接来自 PyBullet
function applyJoints(joints) {
  if (!joints) return;
  for (const [name, angle] of Object.entries(joints)) {
    const joint = robotJoints[name];
    if (joint) joint.object.quaternion.setFromAxisAngle(joint.axis, angle);
  }
}

// ------------------------------------------------------------------ overlays
const pathGeometry = new THREE.BufferGeometry();
const pathLine = new THREE.Line(
  pathGeometry,
  new THREE.LineBasicMaterial({ color: 0x22d3ee, transparent: true, opacity: 0.95 })
);
scene.add(pathLine);

const lidarGeometry = new THREE.BufferGeometry();
const lidarPoints = new THREE.Points(
  lidarGeometry,
  new THREE.PointsMaterial({ color: 0xfacc15, size: 0.035, sizeAttenuation: true })
);
scene.add(lidarPoints);

const goalRing = new THREE.Mesh(
  new THREE.RingGeometry(0.20, 0.26, 28),
  new THREE.MeshBasicMaterial({ color: 0x34d399, transparent: true, opacity: 0.9, side: THREE.DoubleSide })
);
goalRing.rotation.x = -Math.PI / 2;
goalRing.position.y = 0.03;
goalRing.visible = false;
scene.add(goalRing);

const obstacleGroup = new THREE.Group();
scene.add(obstacleGroup);
let obstacleSignature = '';

const previewMat = new THREE.MeshStandardMaterial({
  color: 0xf97316, transparent: true, opacity: 0.45, roughness: 0.8,
});
const previewBox = new THREE.Mesh(new THREE.BoxGeometry(1, 1, 1), previewMat);
previewBox.visible = false;
scene.add(previewBox);

// ------------------------------------------------------------------ helpers
const tmpVec = new THREE.Vector3();
let lastGoal = null;

function bulletToThree(x, y, z = 0) {
  return new THREE.Vector3(x, z, -y);
}

function updatePath(path) {
  if (!path || path.length < 2) {
    pathGeometry.setFromPoints([new THREE.Vector3()]);
    pathLine.visible = false;
    goalRing.visible = false;
    return;
  }
  const points = path.map(([x, y]) => new THREE.Vector3(x, 0.035, -y));
  pathGeometry.setFromPoints(points);
  pathLine.visible = true;
  const last = path[path.length - 1];
  goalRing.position.set(last[0], 0.035, -last[1]);
  goalRing.visible = true;
}

function updateLidar(points, robot) {
  if (!points || !points.length) {
    lidarGeometry.setFromPoints([]);
    return;
  }
  const arr = [];
  for (const [x, y] of points) {
    const d = Math.hypot(x - robot.x, y - robot.y);
    if (d >= 5.9) continue;
    arr.push(new THREE.Vector3(x, lidarHeight, -y));
  }
  lidarGeometry.setFromPoints(arr);
}

function updateObstacles(obstacles) {
  const signature = JSON.stringify(obstacles || []);
  if (signature === obstacleSignature) return;
  obstacleSignature = signature;
  while (obstacleGroup.children.length) {
    const child = obstacleGroup.children[0];
    obstacleGroup.remove(child);
    child.geometry.dispose();
    child.material.dispose();
  }
  for (const item of obstacles || []) {
    const width = item.max_x - item.min_x;
    const depth = item.max_y - item.min_y;
    const height = item.height || 0.8;
    const mesh = new THREE.Mesh(
      new THREE.BoxGeometry(width, height, depth),
      new THREE.MeshStandardMaterial({
        color: 0xf97316, transparent: true, opacity: 0.5, roughness: 0.7,
      })
    );
    mesh.position.set(
      (item.min_x + item.max_x) / 2,
      height / 2,
      -(item.min_y + item.max_y) / 2
    );
    const edges = new THREE.LineSegments(
      new THREE.EdgesGeometry(mesh.geometry),
      new THREE.LineBasicMaterial({ color: 0xfb923c })
    );
    mesh.add(edges);
    obstacleGroup.add(mesh);
  }
}

function setStatus(id, text) {
  const element = document.getElementById(id);
  if (element) element.textContent = text;
}

let toastTimer = null;
function toast(message, duration = 2600) {
  const element = document.getElementById('toast');
  element.textContent = message;
  element.classList.add('show');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => element.classList.remove('show'), duration);
}

async function api(path, options) {
  const url = path.replace(/^\.\/api\/sim/, API_BASE);
  const response = await fetch(url, {
    headers: { 'Content-Type': 'application/json' },
    ...options,
  });
  const data = await response.json().catch(() => ({}));
  if (!response.ok || data.ok === false) {
    throw new Error(data.error || `请求失败 (${response.status})`);
  }
  return data;
}

// ------------------------------------------------------------------ scene load
async function loadScene() {
  info = await api('./api/sim/info');
  const engine = `${info.engine} · ${info.physics_hz} Hz`;
  setStatus('engine', engine);
  if (info.sensors && info.sensors.lidar && info.sensors.lidar.z) {
    lidarHeight = info.sensors.lidar.z;
  }

  const b = info.scene.three_bounds;
  bounds = {
    minX: b[0][0], maxX: b[1][0],
    minZ: b[0][2], maxZ: b[1][2],
    centerX: (b[0][0] + b[1][0]) / 2,
    centerZ: (b[0][2] + b[1][2]) / 2,
  };

  camera.position.set(bounds.centerX + 7.5, 9.0, bounds.centerZ + 11.0);
  controls.target.set(bounds.centerX, 1.1, bounds.centerZ);
  controls.update();

  const loader = new GLTFLoader();
  const gltf = await loader.loadAsync(`${ASSET_BASE}/japanese-classroom/scene.gltf`);
  model = gltf.scene;
  model.position.y = info.scene.floor_offset;
  model.traverse((child) => {
    if (child.isMesh) {
      child.castShadow = false;
      child.receiveShadow = false;
      if (child.material) {
        child.material.side = THREE.FrontSide;
      }
    }
  });
  scene.add(model);

  const ground = new THREE.Mesh(
    new THREE.PlaneGeometry(80, 80),
    new THREE.MeshStandardMaterial({ color: 0x101827, roughness: 1.0 })
  );
  ground.rotation.x = -Math.PI / 2;
  ground.position.y = -0.012;
  scene.add(ground);

  const width = bounds.maxX - bounds.minX;
  const depth = bounds.maxZ - bounds.minZ;
  floorPlane = new THREE.Mesh(
    new THREE.PlaneGeometry(width + 10, depth + 10),
    new THREE.MeshBasicMaterial({ transparent: true, opacity: 0.0, depthWrite: false })
  );
  floorPlane.rotation.x = -Math.PI / 2;
  floorPlane.position.set(bounds.centerX, 0.02, bounds.centerZ);
  scene.add(floorPlane);
}

// ------------------------------------------------------------------ state loop
let polling = false;
let latestRobot = null;
let firstState = true;
const targetPos = new THREE.Vector3();
const targetYaw = { value: 0 };

async function pollState() {
  if (polling) return;
  polling = true;
  try {
    const s = await api('./api/sim/state');
    latestRobot = s.robot;
    setStatus('pose', `${s.robot.x.toFixed(2)}, ${s.robot.y.toFixed(2)} / ${(s.robot.yaw * 180 / Math.PI).toFixed(0)}°`);
    setStatus('speed', `${s.robot.v.toFixed(2)} m/s`);
    setStatus('pathinfo', `${s.path ? s.path.length : 0} 点 · #${s.path_index || 0}`);
    setStatus('runstate', s.navigating ? '导航中' : (s.arrived ? '已到达' : '待机'));

    targetPos.set(s.robot.x, s.robot.z, -s.robot.y);
    targetYaw.value = s.robot.yaw;
    applyJoints(s.robot.joints);
    robotGroup.visible = robotReady;
    if (firstState) {
      robotGroup.position.copy(targetPos);
      robotGroup.rotation.y = s.robot.yaw;
      firstState = false;
    }

    updatePath(s.path);
    updateLidar(s.lidar, s.robot);
    updateObstacles(s.obstacles);
  } catch (error) {
    setStatus('runstate', '连接断开');
  } finally {
    polling = false;
  }
}

function smoothRobot() {
  if (!latestRobot) return;
  robotGroup.position.lerp(targetPos, 0.28);
  let current = robotGroup.rotation.y;
  let delta = targetYaw.value - current;
  while (delta > Math.PI) delta -= Math.PI * 2;
  while (delta < -Math.PI) delta += Math.PI * 2;
  robotGroup.rotation.y = current + delta * 0.28;
}

// ------------------------------------------------------------------ picking
const raycaster = new THREE.Raycaster();
const pointer = new THREE.Vector2();
const groundPoint = new THREE.Vector3();

function pickGround(event) {
  const rect = canvas.getBoundingClientRect();
  pointer.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
  pointer.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;
  raycaster.setFromCamera(pointer, camera);
  if (!floorPlane) return null;
  const hits = raycaster.intersectObject(floorPlane, false);
  return hits.length ? hits[0].point : null;
}

async function planTo(point) {
  lastGoal = point.clone();
  try {
    const data = await api('./api/sim/plan', {
      method: 'POST',
      body: JSON.stringify({ x: point.x, y: -point.z }),
    });
    updatePath(data.path);
    toast(`已规划 ${data.path.length} 个路径点`);
  } catch (error) {
    goalRing.visible = false;
    toast(error.message);
  }
}

let obstacleMode = false;
let dragging = false;
let dragStart = null;
let pointerDownScreen = null;

canvas.addEventListener('pointerdown', (event) => {
  if (event.button !== 0) return;
  const point = pickGround(event);
  if (!point) return;
  if (obstacleMode) {
    dragging = true;
    dragStart = point.clone();
    previewBox.visible = true;
    controls.enabled = false;
  } else {
    pointerDownScreen = { x: event.clientX, y: event.clientY };
  }
});

canvas.addEventListener('pointermove', (event) => {
  if (!obstacleMode || !dragging || !dragStart) return;
  const point = pickGround(event);
  if (!point) return;
  const minX = Math.min(dragStart.x, point.x);
  const maxX = Math.max(dragStart.x, point.x);
  const minZ = Math.min(dragStart.z, point.z);
  const maxZ = Math.max(dragStart.z, point.z);
  const w = Math.max(0.1, maxX - minX);
  const d = Math.max(0.1, maxZ - minZ);
  previewBox.scale.set(w, 0.8, d);
  previewBox.position.set((minX + maxX) / 2, 0.4, (minZ + maxZ) / 2);
});

canvas.addEventListener('pointerup', async (event) => {
  if (obstacleMode) {
    if (dragging && dragStart) {
      const point = pickGround(event);
      if (point) {
        const minX = Math.min(dragStart.x, point.x);
        const maxX = Math.max(dragStart.x, point.x);
        const minZ = Math.min(dragStart.z, point.z);
        const maxZ = Math.max(dragStart.z, point.z);
        if (maxX - minX > 0.15 && maxZ - minZ > 0.15) {
          try {
            await api('./api/sim/obstacle', {
              method: 'POST',
              body: JSON.stringify({
                min_x: minX, max_x: maxX,
                min_y: -maxZ, max_y: -minZ,
                height: 0.8,
              }),
            });
            toast('已添加障碍物');
          } catch (error) {
            toast(error.message);
          }
        }
      }
    }
    dragging = false;
    dragStart = null;
    previewBox.visible = false;
    controls.enabled = !obstacleMode;
    return;
  }

  if (pointerDownScreen) {
    const moved = Math.hypot(
      event.clientX - pointerDownScreen.x,
      event.clientY - pointerDownScreen.y
    );
    const point = pickGround(event);
    if (point && moved < 5) {
      await planTo(point);
    }
    pointerDownScreen = null;
  }
});

// ------------------------------------------------------------------ UI
document.getElementById('btn-plan').addEventListener('click', () => {
  if (lastGoal) planTo(lastGoal);
  else toast('先在地面上点选一个目标点');
});

document.getElementById('btn-start').addEventListener('click', async () => {
  try {
    await api('./api/sim/start', { method: 'POST', body: '{}' });
    toast('开始导航');
  } catch (error) {
    toast(error.message);
  }
});

document.getElementById('btn-stop').addEventListener('click', async () => {
  await api('./api/sim/stop', { method: 'POST', body: '{}' });
  toast('已停止');
});

document.getElementById('btn-reset').addEventListener('click', async () => {
  await api('./api/sim/reset', { method: 'POST', body: '{}' });
  lastGoal = null;
  goalRing.visible = false;
  toast('机器人已重置');
});

document.getElementById('btn-clear').addEventListener('click', async () => {
  await api('./api/sim/obstacles/clear', { method: 'POST', body: '{}' });
  toast('障碍物已清空');
});

const obstacleButton = document.getElementById('btn-obstacle');
obstacleButton.addEventListener('click', () => {
  obstacleMode = !obstacleMode;
  obstacleButton.classList.toggle('active', obstacleMode);
  controls.enabled = !obstacleMode;
});

// camera
const cameraPanel = document.getElementById('camera-panel');
const cameraImage = document.getElementById('camera-img');
const cameraToggle = document.getElementById('chk-camera');
let cameraTimer = null;

async function refreshCamera() {
  if (!cameraToggle.checked) return;
  try {
    cameraImage.src = `${API_BASE}/camera.jpg?t=${Date.now()}`;
  } catch (error) {
    /* ignore */
  }
}

cameraToggle.addEventListener('change', () => {
  if (cameraToggle.checked) {
    cameraPanel.classList.remove('hidden');
    refreshCamera();
    cameraTimer = setInterval(refreshCamera, 1400);
  } else {
    cameraPanel.classList.add('hidden');
    clearInterval(cameraTimer);
    cameraTimer = null;
  }
});

document.getElementById('btn-cam-close').addEventListener('click', () => {
  cameraToggle.checked = false;
  cameraToggle.dispatchEvent(new Event('change'));
});

// teleop
const keys = new Set();
const KEY_CMDS = {
  KeyW: { v: 0.4, w: 0 },
  KeyS: { v: -0.4, w: 0 },
  KeyA: { v: 0, w: 0.8 },
  KeyD: { v: 0, w: -0.8 },
};
let teleopTimer = null;

function sendTeleop() {
  let v = 0;
  let w = 0;
  for (const code of keys) {
    if (KEY_CMDS[code]) {
      v += KEY_CMDS[code].v;
      w += KEY_CMDS[code].w;
    }
  }
  api('./api/sim/teleop', {
    method: 'POST',
    body: JSON.stringify({ v, w }),
  }).catch(() => {});
}

function startTeleopLoop() {
  if (teleopTimer) return;
  sendTeleop();
  teleopTimer = setInterval(sendTeleop, 120);
}

function stopTeleopLoop() {
  if (!keys.size && teleopTimer) {
    clearInterval(teleopTimer);
    teleopTimer = null;
    api('./api/sim/teleop', {
      method: 'POST',
      body: JSON.stringify({ v: 0, w: 0 }),
    }).catch(() => {});
  }
}

window.addEventListener('keydown', (event) => {
  if (!KEY_CMDS[event.code] || event.repeat) return;
  keys.add(event.code);
  startTeleopLoop();
});

window.addEventListener('keyup', (event) => {
  if (!KEY_CMDS[event.code]) return;
  keys.delete(event.code);
  stopTeleopLoop();
});

for (const button of document.querySelectorAll('.key')) {
  const code = button.dataset.code;
  const press = (event) => {
    event.preventDefault();
    keys.add(code);
    startTeleopLoop();
  };
  const release = () => {
    keys.delete(code);
    stopTeleopLoop();
  };
  button.addEventListener('pointerdown', press);
  button.addEventListener('pointerup', release);
  button.addEventListener('pointerleave', release);
}

// ------------------------------------------------------------------ render
function animate() {
  requestAnimationFrame(animate);
  controls.update();
  smoothRobot();
  renderer.render(scene, camera);
}

window.addEventListener('resize', () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});

async function boot() {
  try {
    await loadScene();
    try {
      await buildRobot();
    } catch (error) {
      toast(`G1 模型加载失败：${error.message}`, 5000);
    }
    toast('场景已加载：PyBullet 已接管物理仿真');
  } catch (error) {
    toast(`场景加载失败：${error.message}`, 5000);
  }
  animate();
  setInterval(pollState, 70);
}

boot();
