import * as THREE from 'three';
import { STLLoader } from './vendor/jsm/loaders/STLLoader.js';

// 极简 URDF 加载器：只解析本仿真用到的 <link>/<joint>/<visual mesh>
// 返回 { root, joints: { 关节名: { object, axis } }, links }

const num = (text, fallback = 0) => {
  const value = Number.parseFloat(text);
  return Number.isFinite(value) ? value : fallback;
};

const vec3 = (text, fallback = [0, 0, 0]) => {
  if (!text) return fallback;
  const parts = text.trim().split(/\s+/).map(Number);
  return parts.length === 3 && parts.every(Number.isFinite) ? parts : fallback;
};

const colorOf = (text) => {
  const parts = vec3(text, [0.7, 0.7, 0.7]);
  return new THREE.Color(parts[0], parts[1], parts[2]);
};

const tag = (element, name) => [...element.children]
  .find((child) => child.tagName.toLowerCase() === name);

export async function loadURDF(url) {
  const text = await (await fetch(url, { cache: 'force-cache' })).text();
  const doc = new DOMParser().parseFromString(text, 'application/xml');
  const robot = tag(doc, 'robot');
  if (!robot) throw new Error('URDF 解析失败');

  const palette = {};
  for (const element of robot.children) {
    if (element.tagName.toLowerCase() !== 'material') continue;
    const color = tag(element, 'color');
    if (color) palette[element.getAttribute('name')] = colorOf(color.getAttribute('rgba'));
  }

  const links = new Map();
  const joints = [];
  for (const element of robot.children) {
    const kind = element.tagName.toLowerCase();
    if (kind === 'link') links.set(element.getAttribute('name'), element);
    if (kind === 'joint') joints.push(element);
  }

  const childLinks = new Set();
  for (const joint of joints) {
    childLinks.add(tag(joint, 'child').getAttribute('link'));
  }
  const rootName = [...links.keys()].find((name) => !childLinks.has(name));
  if (!rootName) throw new Error('URDF 缺少根 link');

  const linkObjects = {};
  const makeLink = (name, parent) => {
    const object = new THREE.Group();
    object.name = name;
    parent.add(object);
    linkObjects[name] = object;
    return object;
  };

  const rootParent = new THREE.Group();
  const root = makeLink(rootName, rootParent);

  const jointsByParent = new Map();
  for (const joint of joints) {
    const parentName = tag(joint, 'parent').getAttribute('link');
    if (!jointsByParent.has(parentName)) jointsByParent.set(parentName, []);
    jointsByParent.get(parentName).push(joint);
  }

  const jointObjects = {};
  const build = (linkName) => {
    for (const joint of jointsByParent.get(linkName) || []) {
      const pivot = new THREE.Group();
      pivot.name = joint.getAttribute('name');
      const origin = tag(joint, 'origin');
      const xyz = vec3(origin && origin.getAttribute('xyz'));
      const rpy = vec3(origin && origin.getAttribute('rpy'));
      pivot.position.set(xyz[0], xyz[1], xyz[2]);
      // URDF 的 rpy 等价于 Rz * Ry * Rx
      pivot.rotation.set(rpy[0], rpy[1], rpy[2], 'ZYX');
      linkObjects[linkName].add(pivot);

      const axisElement = tag(joint, 'axis');
      const axis = new THREE.Vector3(...vec3(axisElement && axisElement.getAttribute('xyz'), [0, 0, 1]));
      if (axis.lengthSq() < 1e-9) axis.set(0, 0, 1);
      axis.normalize();
      if (joint.getAttribute('type') !== 'fixed') {
        jointObjects[joint.getAttribute('name')] = { object: pivot, axis };
      }

      const childName = tag(joint, 'child').getAttribute('link');
      makeLink(childName, pivot);
      build(childName);
    }
  };
  build(rootName);

  const loader = new STLLoader();
  const cache = new Map();
  const pending = [];

  for (const [linkName, element] of links) {
    for (const visual of element.children) {
      if (visual.tagName.toLowerCase() !== 'visual') continue;
      const origin = tag(visual, 'origin');
      const xyz = vec3(origin && origin.getAttribute('xyz'));
      const rpy = vec3(origin && origin.getAttribute('rpy'));

      const geometry = tag(visual, 'geometry');
      const mesh = geometry && tag(geometry, 'mesh');
      if (!mesh) continue;

      const scaleText = vec3(mesh.getAttribute('scale'), [1, 1, 1]);
      const filename = mesh.getAttribute('filename');
      const materialElement = tag(visual, 'material');
      const materialName = materialElement ? materialElement.getAttribute('name') : null;
      const material = new THREE.MeshStandardMaterial({
        color: palette[materialName] || new THREE.Color(0x8d939e),
        metalness: 0.18,
        roughness: 0.52,
      });

      // 页面可能以相对路径提供 URDF，这里手工拼接目录，避免 new URL 因缺少 origin 抛错
      const baseDir = url.slice(0, url.lastIndexOf('/') + 1);
      const absolute = filename.startsWith('http') ? filename : baseDir + filename;
      if (!cache.has(absolute)) cache.set(absolute, loader.loadAsync(absolute));
      pending.push(cache.get(absolute).then((geometryData) => {
        const meshObject = new THREE.Mesh(geometryData, material);
        meshObject.position.set(xyz[0], xyz[1], xyz[2]);
        meshObject.rotation.set(rpy[0], rpy[1], rpy[2], 'ZYX');
        meshObject.scale.set(scaleText[0], scaleText[1], scaleText[2]);
        meshObject.castShadow = false;
        linkObjects[linkName].add(meshObject);
      }));
    }
  }

  await Promise.all(pending);
  return { root: rootParent, joints: jointObjects, links: linkObjects };
}
