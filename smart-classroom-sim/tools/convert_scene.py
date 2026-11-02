"""把原始 japanese-classroom GLTF 场景转换成 PyBullet 可直接加载的 OBJ.

约定：
- GLTF 是 Y-up；PyBullet 是 Z-up，因此绕 X 轴旋转 -90°。
- 旋转后把地面平移到 z=0，机器人/路径都以地面为基准。
- 浏览器端仍加载原始 GLTF，只需把模型整体向上平移 floor_offset。
"""
import argparse
import json
import os

import numpy as np
import trimesh

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_GLTF = os.path.join(BASE_DIR, "static", "assets", "japanese-classroom", "scene.gltf")
DEFAULT_OUT = os.path.join(BASE_DIR, "assets")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gltf", default=DEFAULT_GLTF)
    parser.add_argument("--out", default=DEFAULT_OUT)
    args = parser.parse_args()

    os.makedirs(args.out, exist_ok=True)

    scene = trimesh.load(args.gltf, force="scene")
    mesh = scene.to_geometry()
    gltf_bounds = mesh.bounds.copy()

    # Y-up -> Z-up：绕 X 轴 +90°，得到 (x, -z, y)，房间保持正立
    rotation = trimesh.transformations.rotation_matrix(np.pi / 2, [1, 0, 0])
    mesh.apply_transform(rotation)

    floor_offset = float(-gltf_bounds[0][1])
    # 旋转后 z = y_gltf，再向上平移使地面 y=min_y 落到 z=0
    mesh.apply_translation([0, 0, floor_offset])

    obj_path = os.path.join(args.out, "classroom.obj")
    mesh.export(obj_path)

    bullet_bounds = mesh.bounds
    meta = {
        "source_gltf": os.path.relpath(args.gltf, BASE_DIR),
        "obj": os.path.relpath(obj_path, BASE_DIR),
        "floor_offset": floor_offset,
        "gltf_bounds": gltf_bounds.tolist(),
        "bullet_bounds": bullet_bounds.tolist(),
        "three_bounds": [
            [gltf_bounds[0][0], gltf_bounds[0][1] + floor_offset, gltf_bounds[0][2]],
            [gltf_bounds[1][0], gltf_bounds[1][1] + floor_offset, gltf_bounds[1][2]],
        ],
        "vertices": int(len(mesh.vertices)),
        "faces": int(len(mesh.faces)),
        "scale": 1.0,
    }
    meta_path = os.path.join(args.out, "scene_meta.json")
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2, ensure_ascii=False)

    print(f"OBJ: {obj_path}")
    print(f"meta: {meta_path}")
    print(f"bullet bounds: {bullet_bounds.tolist()}")
    print(f"floor_offset (three): {meta['floor_offset']}")


if __name__ == "__main__":
    main()
