"""
face_emotion/face_emotion.py
用 YOLOv8-face 替代 dlib HOG 做人脸检测，
用 DeepFace (FER CNN) 替代几何规则做表情分类。
"""

import cv2 as cv
import numpy as np
from ultralytics import YOLO
from deepface import DeepFace
import os
import json

# ──────────────────────────────────────────────
# 表情映射：DeepFace 原始标签 → 项目中文标签
# ──────────────────────────────────────────────
EMOTION_MAP = {
    'neutral':   '专注',
    'happy':     '开心',
    'surprise':  '惊讶',
    'angry':     '愤怒',
    'sad':       '愤怒',   # 悲伤归入"愤怒"负面类，与原系统保持一致
    'fear':      '惊讶',   # 恐惧归入"惊讶"类
    'disgust':   '愤怒',
}

# DeepFace 分析时目标情绪列表（仅请求需要的动作，提速）
ACTIONS = ['emotion']

# YOLO 模型路径（支持相对路径，首次运行会自动下载权重）
_YOLO_MODEL_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'weights', 'yolov8n-face-lindevs.pt'
)

# ──────────────────────────────────────────────
# 工具函数
# ──────────────────────────────────────────────

def _load_yolo():
    """加载 YOLOv8-face 模型（单例，避免重复加载）"""
    if not hasattr(_load_yolo, '_model'):
        _load_yolo._model = YOLO(_YOLO_MODEL_PATH)
    return _load_yolo._model


def _detect_faces_yolo(frame_bgr):
    """
    用 YOLOv8-face 检测人脸。
    返回: list of (x1, y1, x2, y2, conf)  —— 像素坐标，整数
    """
    model = _load_yolo()
    results = model(frame_bgr, verbose=False, conf=0.4)[0]
    boxes = []
    if results.boxes is not None:
        for box in results.boxes:
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)
            conf = float(box.conf[0].cpu().numpy())
            boxes.append((x1, y1, x2, y2, conf))
    return boxes


def _classify_emotion(face_bgr):
    """
    用 DeepFace (FER CNN) 对裁剪好的人脸图像做表情分类。
    返回: (中文标签, 置信度0-100)
    """
    try:
        result = DeepFace.analyze(
            face_bgr,
            actions=ACTIONS,
            enforce_detection=False,   # 已裁剪好的脸，关闭二次检测
            silent=True
        )
        # DeepFace 返回 list（单张图也是 list）
        if isinstance(result, list):
            result = result[0]

        dominant = result.get('dominant_emotion', 'neutral')
        emotions  = result.get('emotion', {})
        conf      = emotions.get(dominant, 0.0)
        cn_label  = EMOTION_MAP.get(dominant, '专注')
        return cn_label, conf

    except Exception as e:
        print(f'[DeepFace] 分析失败: {e}')
        return '专注', 0.0


# 中文标签 → 英文显示标签（OpenCV 不支持中文）
_DISPLAY_LABEL = {
    '专注': 'Focused',
    '开心': 'Happy',
    '惊讶': 'Surprised',
    '愤怒': 'Angry',
}

def _draw_result(frame, x1, y1, x2, y2, label_cn, conf):
    """在帧上绘制人脸框和标签（使用英文避免乱码）"""
    label_en = _DISPLAY_LABEL.get(label_cn, label_cn)
    cv.rectangle(frame, (x1, y1), (x2, y2), (0, 200, 100), 2)
    text = f'{label_en} {conf:.0f}%'
    (tw, th), _ = cv.getTextSize(text, cv.FONT_HERSHEY_SIMPLEX, 0.7, 2)
    cv.rectangle(frame, (x1, y1 - th - 10), (x1 + tw + 8, y1), (0, 200, 100), -1)
    cv.putText(frame, text, (x1 + 4, y1 - 6),
               cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)


# ──────────────────────────────────────────────
# 主类：视频文件分析（对应原 face_emotion 类）
# ──────────────────────────────────────────────

class face_emotion:
    """
    分析视频文件中的人脸表情，生成带标注的结果视频，并返回统计数据。
    用法与原版完全兼容：
        my_face = face_emotion(input_video, output_video)
        stats   = my_face.learning_face()
    """

    def __init__(self, input_video: str, output_video: str):
        self.input_video  = input_video
        self.output_video = output_video

    def learning_face(self) -> dict:
        """
        逐帧分析视频，输出结果视频，返回统计字典：
        {
          'emotion_count': {'专注': n, '开心': n, '惊讶': n, '愤怒': n, '无人脸': n},
          'attention_score': float,   # 0-100
          'total_frames': int
        }
        """
        cap = cv.VideoCapture(self.input_video)
        if not cap.isOpened():
            raise IOError(f'无法打开视频: {self.input_video}')

        total_frames = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
        fps          = cap.get(cv.CAP_PROP_FPS) or 25.0
        w            = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
        h            = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

        # 使用 mp4v 编码写入临时文件，最终由 app.py 中 ffmpeg 转码为 H.264
        fourcc = cv.VideoWriter_fourcc(*'mp4v')
        writer = cv.VideoWriter(self.output_video, fourcc, fps, (w, h))

        emotion_count = {'专注': 0, '开心': 0, '惊讶': 0, '愤怒': 0, '无人脸': 0}

        # 推理间隔：每 N 帧做一次 DeepFace 推理（提速，中间帧复用上一次结果）
        INFER_EVERY = 3
        last_results = []   # [(x1,y1,x2,y2,label,conf), ...]

        frame_idx = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame_idx += 1

            if frame_idx % INFER_EVERY == 1 or frame_idx == 1:
                # ── 真正做推理的帧 ──
                boxes = _detect_faces_yolo(frame)
                last_results = []

                if len(boxes) == 0:
                    emotion_count['无人脸'] += 1
                    cv.putText(frame, 'No Face', (20, 50),
                               cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                else:
                    for (x1, y1, x2, y2, _conf) in boxes:
                        # 裁剪人脸 ROI（加边距防止越界）
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
                        emotion_count[label_cn] += 1

                    for (x1, y1, x2, y2, label_cn, conf) in last_results:
                        _draw_result(frame, x1, y1, x2, y2, label_cn, conf)
            else:
                # ── 复用上一帧的推理结果 ──
                if len(last_results) == 0:
                    emotion_count['无人脸'] += 1
                    cv.putText(frame, 'No Face', (20, 50),
                               cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                else:
                    for (x1, y1, x2, y2, label_cn, conf) in last_results:
                        emotion_count[label_cn] += 1
                        _draw_result(frame, x1, y1, x2, y2, label_cn, conf)

            writer.write(frame)

        cap.release()
        writer.release()

        # ── 计算专注度 ──
        face_frames = total_frames - emotion_count['无人脸']
        if face_frames > 0:
            attention_score = round(
                (emotion_count['专注'] + emotion_count['开心']) / face_frames * 100, 1
            )
        else:
            attention_score = 0.0

        return {
            'emotion_count':   emotion_count,
            'attention_score': attention_score,
            'total_frames':    total_frames,
        }