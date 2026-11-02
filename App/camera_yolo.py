"""
camera_yolo.py  ── 放在项目根目录（与 app.py 同级）
替换 app.py 中 generate_camera_frames() 函数内的 dlib 实现。
将本文件的 generate_camera_frames_yolo() 直接粘贴进 app.py 即可。
"""

import cv2 as cv
import threading
from face_emotion.face_emotion import (
    _load_yolo,
    _detect_faces_yolo,
    _classify_emotion,
    _draw_result,
)

# ── 摄像头状态（与 app.py 中原有的 camera_state / camera_lock 共用）──
# 无需重复定义，直接在 app.py 中引用。


def generate_camera_frames_yolo(camera_state, camera_lock):
    """
    替代原 generate_camera_frames()。
    参数:
        camera_state  —— app.py 中的全局字典
        camera_lock   —— app.py 中的 threading.Lock()
    用法（在 app.py 中）:
        from camera_yolo import generate_camera_frames_yolo
        # 然后把 /videoFeed 路由改为调用此函数
    """

    # ── 预加载模型（避免第一帧卡顿）──
    _load_yolo()

    with camera_lock:
        camera_state['running'] = True
        camera_state['cap'] = cv.VideoCapture(0)
        camera_state['emotion_count'] = {
            '专注': 0, '开心': 0, '惊讶': 0, '愤怒': 0, '无人脸': 0
        }
        camera_state['total_frames'] = 0

    INFER_EVERY = 2          # 每2帧推理一次，平衡实时性与 CPU 占用
    last_results = []        # [(x1,y1,x2,y2,label,conf)]
    frame_idx    = 0

    while True:
        with camera_lock:
            if not camera_state['running']:
                break
            cap = camera_state['cap']

        ret, frame = cap.read()
        if not ret:
            break

        with camera_lock:
            camera_state['total_frames'] += 1
            tf = camera_state['total_frames']

        frame_idx += 1
        h, w = frame.shape[:2]

        if frame_idx % INFER_EVERY == 1 or frame_idx == 1:
            # ── 推理帧 ──
            boxes = _detect_faces_yolo(frame)
            last_results = []

            if len(boxes) == 0:
                with camera_lock:
                    camera_state['emotion_count']['无人脸'] += 1
                    camera_state['current_emotion'] = '无人脸'
                    camera_state['face_count'] = 0
                cv.putText(frame, 'No Face', (20, 50),
                           cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            else:
                for (x1, y1, x2, y2, _conf) in boxes:
                    pad = 10
                    fx1 = max(0, x1 - pad)
                    fy1 = max(0, y1 - pad)
                    fx2 = min(w, x2 + pad)
                    fy2 = min(h, y2 + pad)
                    face_roi = frame[fy1:fy2, fx1:fx2]
                    if face_roi.size == 0:
                        continue
                    label_cn, conf = _classify_emotion(face_roi)
                    last_results.append((x1, y1, x2, y2, label_cn, conf))

                with camera_lock:
                    ec = camera_state['emotion_count']
                    for (_, _, _, _, label_cn, _) in last_results:
                        ec[label_cn] += 1
                    camera_state['current_emotion'] = last_results[-1][4] if last_results else '专注'
                    camera_state['face_count'] = len(last_results)

                for item in last_results:
                    _draw_result(frame, *item)
        else:
            # ── 复用帧 ──
            if not last_results:
                with camera_lock:
                    camera_state['emotion_count']['无人脸'] += 1
                    camera_state['current_emotion'] = '无人脸'
                    camera_state['face_count'] = 0
                cv.putText(frame, 'No Face', (20, 50),
                           cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            else:
                with camera_lock:
                    ec = camera_state['emotion_count']
                    for (_, _, _, _, label_cn, _) in last_results:
                        ec[label_cn] += 1
                    camera_state['face_count'] = len(last_results)
                for item in last_results:
                    _draw_result(frame, *item)

        # ── 实时专注度 ──
        with camera_lock:
            ec  = camera_state['emotion_count']
            tf  = camera_state['total_frames']
            ff  = tf - ec['无人脸']
            if ff > 0:
                camera_state['attention_score'] = round(
                    (ec['专注'] + ec['开心']) / ff * 100, 1
                )

        # ── MJPEG 推流 ──
        ret, buffer = cv.imencode('.jpg', frame, [cv.IMWRITE_JPEG_QUALITY, 80])
        if not ret:
            continue
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n'
               + buffer.tobytes() + b'\r\n')

    with camera_lock:
        if camera_state['cap']:
            camera_state['cap'].release()
            camera_state['cap'] = None
        camera_state['running'] = False
