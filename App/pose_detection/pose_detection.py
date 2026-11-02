import os

import cv2
from ultralytics import YOLO

class pose_detection:
    def __init__(self, input_video, output_video, yolo=None):
        print("姿态识别")
        self.input_video = input_video
        self.output_video = output_video
        model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'yolov8x-pose-p6.pt')
        self.yolo = yolo or YOLO(model_path)
    #     learning_pose
    def learning_pose(self):
        video_path = self.input_video  # 输入视频地址
        cap = cv2.VideoCapture(video_path)  # 创建一个 VideoCapture 对象，用于从视频文件中读取帧
        # 获取视频帧的维度
        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))
        # 创建VideoWriter对象
        fourcc = cv2.VideoWriter.fourcc(*"X264")  # 这个视频编码可以
        out = cv2.VideoWriter(self.output_video, fourcc, 30.0,
                              (frame_width, frame_height))  # 保存检测后视频的地址

        while cap.isOpened():
            status, frame = cap.read()  # 使用 cap.read() 从视频中读取每一帧
            if not status:
                break
            result = self.yolo.predict(source=frame, save=False,  conf=0.01,)
            result = result[0]
            anno_frame = result.plot()
            # cv2.imshow('行人', anno_frame)
            out.write(anno_frame)  # 写入保存
            # 注释的框架是通过调用 result.plot() 获得的，它会在框架上绘制边界框和标签。
            # 带注释的框架使用 cv2.imshow() 窗口名称“行人”显示。

        cap.release()
        cv2.destroyAllWindows()
        # video_yolo_path = 'C:\\Users\\25055\Desktop\\6-teacher.mp4'
        # return video_yolo_path

if __name__ == '__main__':
    my_pose = pose_detection(input_video="9月15日(5).mp4", output_video="6-teacher.mp4")
    my_pose.learning_pose()
