import os.path
import urllib.error
import urllib.request
import uuid
from urllib.parse import urljoin
import mimetypes  # 新增：识别视频文件的MIME类型
from functools import wraps

import redis
from flask import request, jsonify, send_from_directory, Response, json, session
from flask import Flask
from flask_cors import CORS  # 新增：跨域支持

import voice_recognition
import cv2 as cv
import redis_test
import constant

redis_client = redis.Redis(host='localhost', port=6379, db=0, protocol=2)
import sqlite3

app = Flask(__name__)
app.secret_key = os.environ.get('DSAVD_SECRET_KEY', os.urandom(32))

# ==================== 核心修复1：配置绝对路径（解决路径漂移） ====================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # app.py所在目录
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
RESULT_FOLDER = os.path.join(BASE_DIR, 'result')
REPORT_FOLDER = os.path.join(BASE_DIR, 'report')
VIDEO_FOLDER = os.path.join(BASE_DIR, 'dsvideo')

# 确保文件夹存在
for folder in [UPLOAD_FOLDER, RESULT_FOLDER, REPORT_FOLDER, VIDEO_FOLDER]:
    if not os.path.isdir(folder):
        os.makedirs(folder)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER
app.config['REPORT_FOLDER'] = REPORT_FOLDER
app.config['VIDEO_FOLDER'] = VIDEO_FOLDER

# ==================== 核心修复2：添加跨域配置（解决403） ====================
CORS(
    app,
    resources={
        r"/expressionRecognition": {"origins": "*", "methods": ["GET", "POST"], "allow_headers": "*"},
        r"/result/*": {"origins": "*", "methods": ["GET"], "allow_headers": "*"},
        r"/uploads/*": {"origins": "*", "methods": ["GET"], "allow_headers": "*"},
        r"/report/*": {"origins": "*", "methods": ["GET", "POST"], "allow_headers": "*"},
        r"/uploadVideo": {"origins": "*", "methods": ["POST"], "allow_headers": "*"},
        r"/deleteVideo": {"origins": "*", "methods": ["POST"], "allow_headers": "*"},
        r"/videoList": {"origins": "*", "methods": ["GET"], "allow_headers": "*"},
        r"/poseDetection": {"origins": "*", "methods": ["POST"], "allow_headers": "*"},
        r"/dsvideo/*": {"origins": "*", "methods": ["GET", "POST"], "allow_headers": "*"},
        r"/login": {"origins": "*", "methods": ["POST"], "allow_headers": "*"},
        r"/register": {"origins": "*", "methods": ["POST"], "allow_headers": "*"},
        r"/*": {"origins": "*"}  # 兜底：允许所有路由跨域（开发环境）
    },
    supports_credentials=True  # 允许携带凭证，解决隐性403
)

global currentUser


@app.route('/')
def main():
    return 'Hello World!'


def random_filename(filename):
    ext = os.path.splitext(filename)[-1]
    return uuid.uuid4().hex + ext


def _get_user_role(username):
    """Get user role from Redis, default to student."""
    if not username:
        return 'student'
    if session.get('username') == username and session.get('role'):
        return session['role']
    if username == 'admin':
        return 'teacher'
    role_data = redis_client.get(constant.USER_ROLE_KEY + username)
    return role_data.decode() if role_data else 'student'


def _is_teacher_user():
    return _get_user_role(session.get('username')) == 'teacher'


def teacher_only(view_func):
    """装饰器：仅允许教师账户访问课堂行为分析相关接口，学生账户返回 403。"""
    @wraps(view_func)
    def wrapped(*args, **kwargs):
        if not _is_teacher_user():
            return jsonify({'message': '该功能仅限教师账户使用，学生账户默认无权访问课堂行为分析。'}), 403
        return view_func(*args, **kwargs)
    return wrapped


@app.route('/uploadVideo', methods=['POST'])
@teacher_only
def upload_video():
    video = request.files.get('video')
    print("上传的原视频 名称： ", video.filename)
    if video.filename == "7.mp4":
        filename = video.filename
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        video.save(filepath)  # 已为绝对路径，无需拼接app.root_path
        file_url = urljoin(request.host_url, f"uploads/{filename}")  # 规范URL拼接
        redis_client.lpush(constant.USER_VIDEOS_KEY + (session.get('username') or 'guest'), file_url)
        return file_url
    if video:
        filename = random_filename(video.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        video.save(filepath)  # 修复：直接用绝对路径保存
        file_url = urljoin(request.host_url, f"uploads/{filename}")  # 规范拼接
        redis_client.lpush(constant.USER_VIDEOS_KEY + (session.get('username') or 'guest'), file_url)
        return file_url
    return '视频上传失败!'


@app.route('/uploads/<path:filename>')
def get_uploads_video(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/result/<path:filename>')
def get_video_result(filename):
    # 1. 拼接绝对路径
    video_abs_path = os.path.join(app.config['RESULT_FOLDER'], filename)
    print(f"【调试】视频路径：{video_abs_path}，存在：{os.path.exists(video_abs_path)}")

    # 2. 校验文件存在
    if not os.path.exists(video_abs_path):
        return f"文件不存在：{video_abs_path}", 404

    # 3. 获取文件基础信息
    file_size = os.path.getsize(video_abs_path)
    mime_type, _ = mimetypes.guess_type(video_abs_path)
    if mime_type is None:
        mime_type = 'video/mp4'

    # 4. 处理分段请求（核心修复：正确计算分段的Content-Length）
    range_header = request.headers.get('Range', None)
    if range_header:
        # 解析Range（格式：bytes=0-1024）
        range_part = range_header.replace('bytes=', '').split('-')
        byte1 = int(range_part[0]) if range_part[0].strip() else 0
        byte2 = int(range_part[1]) if range_part[1].strip() else file_size - 1

        # 边界校验：防止超出文件范围
        byte1 = max(0, byte1)
        byte2 = min(file_size - 1, byte2)
        segment_length = byte2 - byte1 + 1  # 分段数据的实际长度（关键！）

        # 读取分段数据
        with open(video_abs_path, 'rb') as f:
            f.seek(byte1)
            data = f.read(segment_length)

        # 构建分段响应（修复Content-Length为分段长度）
        response = Response(
            data,
            status=206,
            mimetype=mime_type,
            direct_passthrough=True
        )
        # 响应头修复：仅保留必要头，避免冲突
        response.headers['Content-Range'] = f'bytes {byte1}-{byte2}/{file_size}'
        response.headers['Content-Length'] = str(segment_length)
        response.headers['Accept-Ranges'] = 'bytes'
        response.headers['Content-Type'] = mime_type
        response.headers['Cache-Control'] = 'no-cache'
    else:
        # 核心修复3：完整请求时不手动加头，避免冲突
        response = send_from_directory(
            directory=app.config['RESULT_FOLDER'],
            path=filename,
            mimetype=mime_type
        )

    return response


@app.route('/deleteVideo', methods=['POST'])
def delete_video():
    video = request.form.get('video')
    if video:
        filename = video.split("/")[-1]
        # 清理 uploads\ 或 uploads/ 前缀
        if filename.startswith("uploads\\") or filename.startswith("uploads/"):
            filename = filename.split("\\", 1)[-1] if "\\" in filename else filename.split("/", 1)[-1]
        print("deletefilename " + filename)
        if filename in ["1.mp4", "2.mp4", "3.mp4", "4.mp4", "5.mp4", "6.mp4"]:
            return jsonify("您无权限删除！")
        if filename in ["7.mp4"]:
            # 修复4：使用绝对路径删除
            os.remove(os.path.join(UPLOAD_FOLDER, "7.mp4"))
            video_list = []
            filename_list = ['1.mp4', '2.mp4', '3.mp4', '4.mp4', '5.mp4', '6.mp4']
            for i in filename_list:
                video_list.append(urljoin(request.host_url, f"uploads/{i}"))  # 规范拼接
            if redis_client.exists(constant.USER_VIDEOS_KEY + (session.get('username') or 'guest')):
                redis_client.lrem(constant.USER_VIDEOS_KEY + (session.get('username') or 'guest'), 0, video)
            return jsonify(video_list)
        # 修复4：删除uploads目录下的文件（原代码少了UPLOAD_FOLDER）
        os.remove(os.path.join(UPLOAD_FOLDER, filename))
        video_list = []
        filename_list = ['1.mp4', '2.mp4', '3.mp4', '4.mp4', '5.mp4', '6.mp4']
        for i in filename_list:
            video_list.append(urljoin(request.host_url, f"uploads/{i}"))  # 规范拼接
        if redis_client.exists(constant.USER_VIDEOS_KEY + (session.get('username') or 'guest')):
            redis_client.lrem(constant.USER_VIDEOS_KEY + (session.get('username') or 'guest'), 0, video)
        return jsonify(video_list)
    return "删除失败"


@app.route('/videoList')
def get_video_list():
    video_list = []
    filename_list = ['6.mp4']
    for i in filename_list:
        video_list.append(urljoin(request.host_url, f"uploads/{i}"))  # 规范拼接
    username = (session.get('username') or 'guest')
    if redis_client.exists(constant.USER_VIDEOS_KEY + username):
        user_videoLst = redis_client.lrange(constant.USER_VIDEOS_KEY + username, 0, -1)
        for i in range(len(user_videoLst)):
            user_videoLst[i] = user_videoLst[i].decode()
            video_list.append(user_videoLst[i])
    print(video_list)
    return jsonify(video_list)


@app.route('/poseDetection', methods=['POST'])
@teacher_only
def post_detection_pose():
    video = request.form.get('video')
    filename = video.split("/")[-1]
    print("姿态识别  ", filename)
    if redis_client.exists(constant.POSE_DETECTION_KEY + filename):
        result_filename = redis_client.get(constant.POSE_DETECTION_KEY + filename).decode()
        # 修复5：规范URL拼接
        video_url = urljoin(request.host_url, f"result/{result_filename}")
        return jsonify(video_url)
    input_video = os.path.join(UPLOAD_FOLDER, filename)
    newfile = random_filename(filename)
    output_video = os.path.join(RESULT_FOLDER, newfile)
    try:
        from App.pose_detection.pose_detection import pose_detection
        my_pose = pose_detection(input_video=input_video, output_video=output_video)
        my_pose.learning_pose()
    except Exception as e:
        print(f"发生了一个错误: {e}")
    redis_client.set(constant.POSE_DETECTION_KEY + filename, newfile)
    # 修复5：规范URL拼接
    video_url = urljoin(request.host_url, f"result/{newfile}")
    return jsonify(video_url)


# =============================================
# 表情识别接口（保留原有逻辑，仅修复URL拼接）
# =============================================
@app.route('/expressionRecognition', methods=['POST'])
@teacher_only
def expression_recognition():
    video = request.form.get('video')
    filename = video.split("/")[-1]
    print("表情识别：", filename)

    # ====== 新增：清理filename中的uploads前缀 ======
    if filename.startswith('uploads/') or filename.startswith('uploads\\'):
        filename = filename.split('/', 1)[-1] if '/' in filename else filename.split('\\', 1)[-1]
    print(f"【修正后】纯视频文件名：{filename}")
    # ====== 清理结束 ======

    # ====== 修正后的路径调试打印 ======
    print(f"【调试1】代码运行根目录：{BASE_DIR}")
    video_abs_path = os.path.join(UPLOAD_FOLDER, filename)
    print(f"【调试2】代码读取的视频完整路径：{video_abs_path}")
    print(f"【调试3】文件是否存在：{os.path.exists(video_abs_path)}")
    # 额外调试：OpenCV能否打开视频
    print(f"【调试4】尝试用OpenCV打开视频...")
    cap = cv.VideoCapture(video_abs_path)
    if cap.isOpened():
        total_frames = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
        fps = cap.get(cv.CAP_PROP_FPS)
        width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
        print(f"【调试5】OpenCV打开成功！视频信息：总帧数={total_frames}, FPS={fps}, 分辨率={width}x{height}")
        # 尝试读取第一帧
        ret, frame = cap.read()
        print(f"【调试6】读取第一帧结果：{'成功' if ret else '失败'}")
        cap.release()
    else:
        print(f"【调试5】OpenCV打开视频失败！")
    # ====== 调试代码结束 ======

    # 如果 redis 中已经有分析结果，直接返回缓存
    if redis_client.exists(constant.FACE_EMOTION_KEY + filename):
        result_filename = redis_client.get(constant.FACE_EMOTION_KEY + filename).decode()
        # 修复5：规范URL拼接
        video_url = urljoin(request.host_url, f"result/{result_filename}")

        # 尝试读取缓存的统计数据
        stats_key = constant.FACE_EMOTION_KEY + "stats:" + filename
        if redis_client.exists(stats_key):
            import json as _json
            stats = _json.loads(redis_client.get(stats_key).decode())
        else:
            stats = {"emotion_count": {}, "attention_score": 0, "total_frames": 0}

        return jsonify({
            "videoUrl": video_url,
            "stats": stats
        })

    # ====== 修正后的业务路径 ======
    input_video = os.path.join(UPLOAD_FOLDER, filename)
    newfile = random_filename(filename)
    output_video = os.path.join(RESULT_FOLDER, newfile)

    stats = {"emotion_count": {}, "attention_score": 0, "total_frames": 0}
    try:
        from face_emotion.face_emotion import face_emotion
        my_face = face_emotion(input_video, output_video)
        result = my_face.learning_face()
        stats = result
        print("表情识别统计结果：", stats)
    except Exception as e:
        print(f"表情识别发生错误: {e}")

    # ===== 转码为浏览器可播放的 H.264 格式（使用 ffmpeg） =====
    # OpenCV VideoWriter 默认写出 XVID/mp4v 编码，浏览器不支持，必须转为 H.264
    import subprocess
    import shutil

    print(f"原始视频路径：{output_video}，存在：{os.path.exists(output_video)}")

    # 确定待转码的源文件
    if os.path.exists(output_video) and os.path.getsize(output_video) > 0:
        source_for_transcode = output_video
    else:
        print("识别结果视频不存在或为空，回退使用原始上传视频")
        source_for_transcode = os.path.join(UPLOAD_FOLDER, filename)

    # 转码后的输出文件
    transcoded_file = os.path.join(RESULT_FOLDER, uuid.uuid4().hex + ".mp4")

    try:
        # ffmpeg 转码：H.264 视频 + AAC 音频，faststart 使浏览器可边下边播
        ffmpeg_cmd = [
            "ffmpeg", "-y",
            "-i", source_for_transcode,
            "-vcodec", "libx264",
            "-acodec", "aac",
            "-movflags", "+faststart",
            "-pix_fmt", "yuv420p",
            "-preset", "fast",
            transcoded_file
        ]
        print(f"执行 ffmpeg 转码：{' '.join(ffmpeg_cmd)}")
        proc = subprocess.run(ffmpeg_cmd, capture_output=True, text=True, timeout=300)
        if proc.returncode == 0 and os.path.exists(transcoded_file) and os.path.getsize(transcoded_file) > 0:
            print(f"ffmpeg 转码成功，输出：{transcoded_file}，大小：{os.path.getsize(transcoded_file)} bytes")
            if os.path.exists(output_video) and output_video != source_for_transcode:
                os.remove(output_video)
            newfile = os.path.basename(transcoded_file)
        else:
            print(f"ffmpeg 转码失败，returncode={proc.returncode}")
            print(f"ffmpeg stderr: {proc.stderr[-1000:]}")
            shutil.copy2(source_for_transcode, transcoded_file)
            newfile = os.path.basename(transcoded_file)
    except FileNotFoundError:
        print("未找到 ffmpeg，请先安装 ffmpeg 并加入系统 PATH。直接复制原文件。")
        shutil.copy2(source_for_transcode, transcoded_file)
        newfile = os.path.basename(transcoded_file)
    except subprocess.TimeoutExpired:
        print("ffmpeg 转码超时（>300s），直接复制原文件。")
        shutil.copy2(source_for_transcode, transcoded_file)
        newfile = os.path.basename(transcoded_file)
    # ===== 转码结束 =====

    # 缓存视频文件名和统计数据
    redis_client.set(constant.FACE_EMOTION_KEY + filename, newfile)
    import json as _json
    redis_client.set(constant.FACE_EMOTION_KEY + "stats:" + filename, _json.dumps(stats, ensure_ascii=False))

    # 修复5：规范URL拼接
    video_url = urljoin(request.host_url, f"result/{newfile}")
    return jsonify({
        "videoUrl": video_url,
        "stats": stats
    })


# =============================================
# 以下接口保留原有逻辑，仅修复URL拼接（已标注）
# =============================================
@app.route('/generateReport', methods=['POST'])
@teacher_only
def generate_report():
    from reportlab.lib.pagesizes import A4
    from reportlab.lib import colors
    from reportlab.lib.units import cm
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    import datetime
    import json as _json

    data = request.get_json()
    emotion_count = data.get('emotion_count', {})
    attention_score = data.get('attention_score', 0)
    total_frames = data.get('total_frames', 0)
    video_name = data.get('video_name', '未知视频')

    # 注册中文字体（使用系统字体）
    font_path = os.path.join(BASE_DIR, 'fonts', 'simhei.ttf')
    try:
        pdfmetrics.registerFont(TTFont('SimHei', font_path))
        font_name = 'SimHei'
    except Exception:
        font_name = 'Helvetica'

    report_filename = uuid.uuid4().hex + ".pdf"
    report_path = os.path.join(REPORT_FOLDER, report_filename)

    doc = SimpleDocTemplate(report_path, pagesize=A4,
                            rightMargin=2 * cm, leftMargin=2 * cm,
                            topMargin=2 * cm, bottomMargin=2 * cm)

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle('title', fontName=font_name, fontSize=18,
                                 alignment=1, spaceAfter=12)
    heading_style = ParagraphStyle('heading', fontName=font_name, fontSize=13,
                                   spaceAfter=8, spaceBefore=12)
    body_style = ParagraphStyle('body', fontName=font_name, fontSize=11,
                                spaceAfter=6, leading=18)

    story = []

    # 标题
    story.append(Paragraph("学生课堂学习状态分析报告", title_style))
    story.append(Spacer(1, 0.3 * cm))

    # 基本信息
    now = datetime.datetime.now().strftime("%Y年%m月%d日 %H:%M")
    story.append(Paragraph(f"分析时间：{now}", body_style))
    story.append(Paragraph(f"视频文件：{video_name}", body_style))
    story.append(Paragraph(f"分析总帧数：{total_frames} 帧", body_style))
    story.append(Spacer(1, 0.5 * cm))

    # 专注度评分
    story.append(Paragraph("一、专注度评分", heading_style))
    score_color = "green" if attention_score >= 70 else ("orange" if attention_score >= 40 else "red")
    if attention_score >= 70:
        level = "优秀"
        comment = "该学生在课堂中整体保持较高专注度，学习状态良好。"
    elif attention_score >= 40:
        level = "一般"
        comment = "该学生课堂专注度处于中等水平，建议适当引导提升注意力。"
    else:
        level = "较低"
        comment = "该学生课堂专注度偏低，建议教师加强互动，了解学生状态。"

    story.append(Paragraph(f"专注度得分：<b>{attention_score}分</b>　评级：{level}", body_style))
    story.append(Paragraph(f"评语：{comment}", body_style))
    story.append(Spacer(1, 0.5 * cm))

    # 表情统计
    story.append(Paragraph("二、表情识别统计", heading_style))

    table_data = [["表情类型", "出现帧数", "占比"]]
    face_frames = total_frames - emotion_count.get("无人脸", 0)
    for emotion, count in emotion_count.items():
        if emotion == "无人脸":
            continue
        ratio = f"{round(count / face_frames * 100, 1)}%" if face_frames > 0 else "0%"
        table_data.append([emotion, str(count), ratio])
    table_data.append(["未检测到人脸", str(emotion_count.get("无人脸", 0)), ""])

    table = Table(table_data, colWidths=[5 * cm, 5 * cm, 5 * cm])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#409EFF')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, -1), font_name),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f5f7fa')]),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#c0ccda')),
        ('ROWHEIGHT', (0, 0), (-1, -1), 0.8 * cm),
    ]))
    story.append(table)
    story.append(Spacer(1, 0.5 * cm))

    # 综合建议
    story.append(Paragraph("三、综合建议", heading_style))
    suggestions = []
    if emotion_count.get("愤怒", 0) > face_frames * 0.1:
        suggestions.append("• 检测到较多愤怒表情，建议关注学生情绪状态，适当调整教学节奏。")
    if emotion_count.get("惊讶", 0) > face_frames * 0.15:
        suggestions.append("• 检测到较多惊讶表情，说明课堂中有较多新知识点，可适当放慢讲解速度。")
    if emotion_count.get("开心", 0) > face_frames * 0.2:
        suggestions.append("• 学生开心表情占比较高，课堂氛围积极，建议保持当前教学风格。")
    if emotion_count.get("无人脸", 0) > total_frames * 0.3:
        suggestions.append("• 较多帧未检测到人脸，可能存在学生低头或离开座位的情况，建议加强课堂管理。")
    if not suggestions:
        suggestions.append("• 课堂整体状态良好，继续保持。")

    for s in suggestions:
        story.append(Paragraph(s, body_style))

    story.append(Spacer(1, 1 * cm))
    story.append(Paragraph("—— 智油畅学平台 · 课堂行为分析系统 自动生成", body_style))

    doc.build(story)

    # 修复5：规范URL拼接
    report_url = urljoin(request.host_url, f"report/{report_filename}")
    return jsonify({"reportUrl": report_url})


def _find_latest_deeptutor_assistant_answer():
    import glob
    import json as _json

    deeptutor_workspace_root = r"C:\DeepTutor-main\data\user\workspace\chat"
    event_files = []
    for sub_dir in ["chat", "deep_solve"]:
        event_files.extend(glob.glob(os.path.join(
            deeptutor_workspace_root,
            sub_dir,
            "turn_*",
            "events.jsonl"
        )))
    event_files = sorted(event_files, key=lambda p: os.path.getmtime(p), reverse=True)
    solve_answer_files = glob.glob(os.path.join(
        deeptutor_workspace_root,
        "deep_solve",
        "solve_*",
        "final_answer.md"
    ))

    latest_answer = ''
    latest_timestamp = 0
    latest_source = ''

    for answer_file in solve_answer_files:
        try:
            timestamp = os.path.getmtime(answer_file)
            with open(answer_file, 'r', encoding='utf-8') as f:
                response = f.read().strip()
        except Exception:
            continue

        if response and timestamp >= latest_timestamp:
            latest_answer = response
            latest_timestamp = timestamp
            latest_source = answer_file

    for event_file in event_files:
        try:
            with open(event_file, 'r', encoding='utf-8') as f:
                events = []
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        events.append(_json.loads(line))
                    except Exception:
                        continue
        except Exception:
            continue

        for event in reversed(events):
            metadata = event.get('metadata') or {}
            response = metadata.get('response')
            timestamp = float(event.get('timestamp') or 0)
            if event.get('type') == 'result' and isinstance(response, str) and response.strip():
                if timestamp >= latest_timestamp:
                    latest_answer = response.strip()
                    latest_timestamp = timestamp
                    latest_source = event_file
                break

    return {
        'answer': latest_answer,
        'timestamp': latest_timestamp,
        'source': latest_source,
    }


def _as_number(value, default=0):
    try:
        return float(value)
    except Exception:
        return default


def _pick_count(data, *names):
    for name in names:
        if name in data:
            return _as_number(data.get(name), 0)
    return 0


def _build_learning_suggestions(attention_score, emotion_count, total_frames, tutor_answer):
    face_frames = max(total_frames - _pick_count(emotion_count, '无人脸', '未检测到人脸'), 0)
    suggestions = []

    if attention_score >= 80:
        suggestions.append('课堂专注度表现优秀，可继续保持当前学习节奏，并适当增加拓展性任务。')
    elif attention_score >= 60:
        suggestions.append('课堂专注度总体良好，建议在关键知识点讲解阶段增加短时互动或即时反馈。')
    else:
        suggestions.append('课堂专注度偏低，建议缩短连续讲授时长，穿插问题引导、演示或练习任务。')

    if face_frames > 0:
        confused = _pick_count(emotion_count, '惊讶', '困惑')
        happy = _pick_count(emotion_count, '开心')
        angry = _pick_count(emotion_count, '愤怒')
        if confused / face_frames > 0.15:
            suggestions.append('学生出现较多疑惑或惊讶表情，说明当前知识点可能存在理解门槛，建议补充例题或分步骤讲解。')
        if happy / face_frames > 0.2:
            suggestions.append('学生积极表情占比较高，课堂氛围较好，可以保留当前讲解方式并加入更高阶任务。')
        if angry / face_frames > 0.1:
            suggestions.append('学生负向情绪占比较高，建议关注学习压力或任务难度，及时进行安抚和节奏调整。')

    if tutor_answer:
        suggestions.append('DeepTutor 最新回答可作为后续学习材料，建议教师结合课堂状态挑选其中的步骤、示例或练习安排复盘。')
    else:
        suggestions.append('当前未读取到 DeepTutor 最新回答，建议先完成一次智能对话后再生成更完整的学习报告。')

    return suggestions


@app.route('/generateLearningReport', methods=['POST'])
@teacher_only
def generate_learning_report():
    from reportlab.lib.pagesizes import A4
    from reportlab.lib import colors
    from reportlab.lib.units import cm
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    import datetime
    import re

    def clean_tutor_text(text):
        text = text or ''
        text = re.sub(r'```[\s\S]*?```', ' ', text)
        text = re.sub(r'\$\$[\s\S]*?\$\$', ' ', text)
        text = re.sub(r'\\\[[\s\S]*?\\\]', ' ', text)
        text = re.sub(r'\\begin\{[\s\S]*?\\end\{[^}]+\}', ' ', text)
        text = re.sub(r'\[[^\]]*rag-[^\]]*\]', ' ', text, flags=re.IGNORECASE)
        text = re.sub(r'#+\s*', '', text)
        text = re.sub(r'[*_`>|#\-]+', ' ', text)
        text = re.sub(r'\|[^。\n]{0,120}\|', ' ', text)
        text = re.sub(r'[A-Za-z_./\\{}()[\]=+<>:;]{4,}', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip()
        chinese_parts = re.findall(r'[\u4e00-\u9fff][\u4e00-\u9fff，。！？、；：“”《》（）0-9\s]{4,}', text)
        cleaned = '。'.join(part.strip(' ，。；') for part in chinese_parts if part.strip())
        cleaned = re.sub(r'。+', '。', cleaned).strip('。 ')
        return cleaned

    def summarize_learning_topic(cleaned_text):
        if not cleaned_text:
            return '本次 DeepTutor 对话内容较少，暂未形成明确的知识主题。'
        sentences = re.split(r'[。！？]', cleaned_text)
        picked = []
        total_len = 0
        for sentence in sentences:
            sentence = sentence.strip()
            if len(sentence) >= 12 and sentence not in picked:
                picked.append(sentence)
                total_len += len(sentence)
            if total_len >= 380:
                break
        if not picked:
            return cleaned_text[:400]
        summary = '。'.join(picked)
        return summary[:420].rstrip('，；、 ') + '。'

    data = request.get_json() or {}
    emotion_count = data.get('emotion_count') or {}
    attention_score = _as_number(data.get('attention_score'), 0)
    total_frames = int(_as_number(data.get('total_frames'), 0))
    video_name = data.get('video_name') or '未知视频'

    latest_tutor = _find_latest_deeptutor_assistant_answer()
    tutor_answer = latest_tutor.get('answer') or ''
    tutor_answer_clean = clean_tutor_text(tutor_answer)
    tutor_summary = summarize_learning_topic(tutor_answer_clean)

    font_path = os.path.join(BASE_DIR, 'fonts', 'simhei.ttf')
    try:
        pdfmetrics.registerFont(TTFont('SimHei', font_path))
        font_name = 'SimHei'
    except Exception:
        font_name = 'Helvetica'

    report_filename = uuid.uuid4().hex + '.pdf'
    report_path = os.path.join(REPORT_FOLDER, report_filename)

    doc = SimpleDocTemplate(
        report_path,
        pagesize=A4,
        rightMargin=2 * cm,
        leftMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
    )

    title_style = ParagraphStyle('learningTitle', fontName=font_name, fontSize=18, alignment=1, spaceAfter=16)
    heading_style = ParagraphStyle('learningHeading', fontName=font_name, fontSize=13, spaceAfter=8, spaceBefore=12)
    body_style = ParagraphStyle('learningBody', fontName=font_name, fontSize=11, leading=20, firstLineIndent=22, spaceAfter=8)
    meta_style = ParagraphStyle('learningMeta', fontName=font_name, fontSize=9.5, leading=15, textColor=colors.HexColor('#606266'), spaceAfter=4)
    small_style = ParagraphStyle('learningSmall', fontName=font_name, fontSize=9, leading=14, textColor=colors.HexColor('#606266'))

    story = []
    story.append(Paragraph('学生综合学习评价报告', title_style))
    story.append(Paragraph('课堂行为分析系统 与 DeepTutor 智能学习记录联合生成', small_style))
    story.append(Spacer(1, 0.3 * cm))

    now = datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M')
    story.append(Paragraph(f'生成时间：{now}', meta_style))
    story.append(Paragraph(f'分析视频：{video_name}', meta_style))
    story.append(Paragraph(f'有效分析帧数：{total_frames} 帧', meta_style))

    if latest_tutor.get('timestamp'):
        tutor_time = datetime.datetime.fromtimestamp(latest_tutor['timestamp']).strftime('%Y年%m月%d日 %H:%M')
        story.append(Paragraph(f'DeepTutor 最新学习记录时间：{tutor_time}', meta_style))
    story.append(Spacer(1, 0.3 * cm))

    if attention_score >= 70:
        level = '优秀'
        attention_comment = '课堂专注度较高，能够较稳定地保持学习投入，整体学习状态积极。'
    elif attention_score >= 40:
        level = '一般'
        attention_comment = '课堂专注度处于中等水平，能够完成基本学习跟进，但在持续投入方面仍有提升空间。'
    else:
        level = '较低'
        attention_comment = '课堂专注度偏低，学习过程中可能存在注意力分散、任务难度不匹配或学习兴趣不足等情况。'

    face_frames = total_frames - int(_pick_count(emotion_count, '无人脸', '未检测到人脸'))
    face_frames = max(face_frames, 0)
    focus_count = _pick_count(emotion_count, '专注')
    happy_count = _pick_count(emotion_count, '开心')
    surprised_count = _pick_count(emotion_count, '惊讶')
    angry_count = _pick_count(emotion_count, '愤怒')

    focus_ratio = round(focus_count / face_frames * 100, 1) if face_frames else 0
    happy_ratio = round(happy_count / face_frames * 100, 1) if face_frames else 0
    surprised_ratio = round(surprised_count / face_frames * 100, 1) if face_frames else 0
    angry_ratio = round(angry_count / face_frames * 100, 1) if face_frames else 0

    story.append(Paragraph('一、课堂学习状态评价', heading_style))
    story.append(Paragraph(
        f'从课堂行为识别结果看，学生本次学习的专注度得分为 {attention_score:g} 分，综合等级为“{level}”。{attention_comment}'
        f'在有效识别画面中，专注表情约占 {focus_ratio}%，积极表情约占 {happy_ratio}%，疑惑或惊讶表情约占 {surprised_ratio}%，负向情绪表情约占 {angry_ratio}%。'
        '整体来看，该生在课堂中具备一定的学习投入基础，教师可结合具体知识点难度继续观察其理解状态与情绪变化。',
        body_style,
    ))

    story.append(Paragraph('二、学习内容理解情况', heading_style))
    if tutor_answer_clean:
        story.append(Paragraph(
            f'结合 DeepTutor 最近一次学习记录，学生当前接触的主要内容可概括为：{tutor_summary}'
            '从内容特征看，该部分知识具有一定的概念密度和推理要求，学生不仅需要理解基本定义，还需要能够将相关方法迁移到具体问题情境中。'
            '因此，后续学习中应避免只停留在结论记忆层面，而应通过例题、对比和复述来巩固理解。',
            body_style,
        ))
    else:
        story.append(Paragraph(
            '本次未读取到有效的 DeepTutor 学习回答内容，因此报告主要依据课堂行为数据进行评价。建议学生完成一次 DeepTutor 学习对话后，再生成更完整的学习分析报告。',
            body_style,
        ))

    story.append(Paragraph('三、综合教师评语', heading_style))
    if attention_score >= 70:
        teacher_comment = (
            '该生本次课堂表现较为稳定，能够较好地跟随课堂节奏完成学习任务。'
            '从表情和专注度结果看，学生具备较好的学习自控力，对课堂内容保持了较高关注。'
            '建议教师在后续教学中适当增加思考性问题或拓展任务，引导学生从理解知识进一步过渡到应用知识。'
        )
    elif attention_score >= 40:
        teacher_comment = (
            '该生本次课堂表现总体平稳，但专注度仍存在波动。'
            '学生能够参与学习过程，但在持续关注和深度思考方面还需要进一步引导。'
            '建议教师在讲解关键知识点时增加阶段性提问、板书梳理或即时练习，帮助学生及时确认理解情况。'
        )
    else:
        teacher_comment = (
            '该生本次课堂投入程度不足，学习状态需要重点关注。'
            '建议教师先判断学生是因为知识难度较高、课堂节奏较快，还是因为学习兴趣不足而出现注意力分散。'
            '后续可采用更短的任务单元、更多互动反馈和更明确的学习目标，帮助学生逐步恢复学习投入。'
        )
    story.append(Paragraph(teacher_comment, body_style))

    story.append(Paragraph('四、后续学习建议', heading_style))
    suggestions = _build_learning_suggestions(attention_score, emotion_count, total_frames, tutor_answer)
    suggestion_text = '后续建议从以下几个方面开展辅导：' + '；'.join(suggestions[:4]) + '。'
    story.append(Paragraph(suggestion_text, body_style))

    story.append(Spacer(1, 0.8 * cm))
    story.append(Paragraph('本报告由课堂行为分析结果与 DeepTutor 学习记录自动生成，供教师开展学习诊断、课后复盘和个性化辅导参考。', small_style))

    doc.build(story)
    report_url = urljoin(request.host_url, f'report/{report_filename}')
    return jsonify({'reportUrl': report_url, 'deeptutorFound': bool(tutor_answer)})
@app.route('/report/<path:filename>')
def get_report(filename):
    return send_from_directory(app.config['REPORT_FOLDER'], filename)


@app.route('/reportList')
def get_report_list():
    report_list = []
    for filename in os.listdir(REPORT_FOLDER):
        # 修复5：规范URL拼接
        file_url = urljoin(request.host_url, f"report/{filename}")
        report_list.append(file_url)
    return jsonify(report_list)


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['registerName']
    password = data['password']
    role = data.get('role', 'student')
    try:
        from werkzeug.security import generate_password_hash
        conn = _get_mysql_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT id FROM app_user WHERE username = %s", (username,))
            if cursor.fetchone():
                conn.close()
                return jsonify('该用户名已被注册！')
            cursor.execute(
                "INSERT INTO app_user (username, password_hash, role) VALUES (%s, %s, %s)",
                (username, generate_password_hash(password), role)
            )
        conn.commit()
        conn.close()
        return jsonify('注册成功！')
    except Exception as error:
        print(f'MySQL 注册不可用，回退到 Redis: {error}')
        if redis_client.exists(constant.USER_INFO_KEY + username):
            return jsonify('该用户名已被注册！')
        redis_client.set(constant.USER_INFO_KEY + username, password)
        redis_client.set(constant.USER_ROLE_KEY + username, role)
        return jsonify('注册成功！')


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['loginName']
    password = data['password']
    try:
        from werkzeug.security import check_password_hash
        conn = _get_mysql_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT username, password_hash, role FROM app_user WHERE username = %s", (username,))
            user = cursor.fetchone()
        conn.close()
        if user and check_password_hash(user['password_hash'], password):
            session['username'] = username
            session['role'] = user['role']
            return jsonify({'message': '登录成功！', 'role': user['role'], 'username': username})
        if user:
            return jsonify('密码错误！')
    except Exception as error:
        print(f'MySQL 登录不可用，尝试 Redis 兼容账号: {error}')

    if redis_client.exists(constant.USER_INFO_KEY + username):
        if redis_client.get(constant.USER_INFO_KEY + username).decode() == password:
            session['username'] = username
            session['role'] = _get_user_role(username)
            return jsonify({'message': '登录成功！', 'role': session['role'], 'username': username})
        return jsonify('密码错误！')
    return jsonify('用户名或密码错误！')


@app.route('/forgetpassword', methods=['POST'])
def forgetPassword():
    data = request.get_json()
    username = data['username']
    newpassword = data['newPassword']
    try:
        from werkzeug.security import generate_password_hash
        conn = _get_mysql_connection()
        with conn.cursor() as cursor:
            changed = cursor.execute(
                "UPDATE app_user SET password_hash = %s WHERE username = %s",
                (generate_password_hash(newpassword), username)
            )
        conn.commit()
        conn.close()
        if changed:
            return jsonify('密码修改成功!')
    except Exception as error:
        print(f'MySQL 密码修改不可用，尝试 Redis 兼容账号: {error}')
    if redis_client.exists(constant.USER_INFO_KEY + username):
        redis_client.set(constant.USER_INFO_KEY + username, newpassword)
        return jsonify('密码修改成功!')
    return jsonify('不存在该用户名！')


@app.route('/voiceRecognition', methods=['get'])
def voice_Recognition():
    video = os.path.join(BASE_DIR, "voice_recognition", "2.mp4")  # 修复：绝对路径
    res = ""
    try:
        from App.voice_recognition.voice_recognition import voice_recognition
        my_voice = voice_recognition(input_video=video)
        res = my_voice.speech_to_text()
    except Exception as e:
        res = f"发生了一个错误: {e}"
    return jsonify(res)


@app.route('/dsvideo/<id1>/<id2>')
def get_video(id1, id2):
    print(id1, id2)
    return send_from_directory(os.path.join(VIDEO_FOLDER, id1), id2)  # 修复：绝对路径


@app.route('/dsvideo', methods=['POST'])
def video():
    data = request.get_json()
    id1 = data['id1']
    id2 = data['id2']
    id1 = str(id1)
    id2 = str(id2) + ".mp4"
    # 修复5：规范URL拼接
    video_url = urljoin(request.host_url, f"dsvideo/{id1}/{id2}")
    return video_url


@app.route('/exam', methods=['POST'])
def exam():
    data = request.get_json()
    chapter = data['chapter']
    subchapter = data['subchapter']
    # 修复：绝对路径连接数据库
    db_path = os.path.join(BASE_DIR, 'sqlite3db', 'dsavd.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM exam WHERE chapter = ? AND subchapter = ?", (chapter, subchapter))
    result = cursor.fetchall()
    result = [
        {'id': row[0], 'question': row[1], 'option1': row[2], 'option2': row[3], 'option3': row[4],
         'option4': row[5], 'correct_answer': row[6], 'answer_analy': row[7], 'question_type': row[8]}
        for row in result]
    cursor.close()
    conn.close()
    return jsonify(result)


@app.route('/examRecord', methods=['POST'])
def exam_record():
    data = request.get_json()
    username = data['username']
    chapter = data['chapter']
    subchapter = data['subchapter']
    score = data['score']
    # 修复：绝对路径连接数据库
    db_path = os.path.join(BASE_DIR, 'sqlite3db', 'dsavd.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS exam_record (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            username TEXT NOT NULL, chapter TEXT NOT NULL, subchapter TEXT NOT NULL,
            score TEXT NOT NULL, created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("SELECT * FROM exam_record WHERE username = ? AND chapter = ? AND subchapter = ?",
                   (username, chapter, subchapter))
    result = cursor.fetchall()
    if result:
        cursor.execute("DELETE FROM exam_record WHERE username =? AND chapter =? AND subchapter =?",
                       (username, chapter, subchapter))
    cursor.execute("INSERT INTO exam_record (username, chapter, subchapter, score) VALUES (?,?,?,?)",
                   (username, chapter, subchapter, score))
    conn.commit()
    cursor.close()
    conn.close()
    try:
        mysql_conn = _get_mysql_connection()
        with mysql_conn.cursor() as mysql_cursor:
            mysql_cursor.execute("""
                INSERT INTO exam_answer_record (username, chapter, subchapter, score)
                VALUES (%s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE score = VALUES(score), updated_time = CURRENT_TIMESTAMP
            """, (username, chapter, subchapter, score))
        mysql_conn.commit()
        mysql_conn.close()
    except Exception as error:
        print(f'答题记录同步到 MySQL 失败: {error}')
    return jsonify("ok")


@app.route('/examRecordCount', methods=['POST'])
def exam_record_count():
    data = request.get_json()
    chapter = data['chapter']
    subchapter = data['subchapter']
    # 修复：绝对路径连接数据库
    db_path = os.path.join(BASE_DIR, 'sqlite3db', 'dsavd.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT username) FROM exam_record WHERE chapter = ? AND subchapter = ?",
                   (chapter, subchapter))
    count = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(count)


@app.route('/getAverageScore', methods=['POST'])
def get_average_score():
    data = request.get_json()
    chapter = data['chapter']
    subchapter = data['subchapter']
    # 修复：绝对路径连接数据库
    db_path = os.path.join(BASE_DIR, 'sqlite3db', 'dsavd.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT username) FROM exam_record WHERE chapter = ? AND subchapter = ?",
                   (chapter, subchapter))
    renshu = cursor.fetchone()[0]
    cursor.execute("SELECT SUM(score) FROM exam_record WHERE chapter = ? AND subchapter = ?", (chapter, subchapter))
    sumScore = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(round(sumScore / renshu, 2))


@app.route('/feedback', methods=['POST'])
def feedback():
    data = request.get_json()
    email = data['email']
    content = data['content']
    # 修复：绝对路径连接数据库
    db_path = os.path.join(BASE_DIR, 'sqlite3db', 'dsavd.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO feedback (email, content) VALUES (?,?)", (email, content))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify('ok！')


@app.route('/hasExam', methods=['POST'])
def has_exam():
    data = request.get_json()
    username = data['username']
    chapter = data['chapter']
    subchapter = data['subchapter']
    # 修复：绝对路径连接数据库
    db_path = os.path.join(BASE_DIR, 'sqlite3db', 'dsavd.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM exam_record WHERE username = ? AND chapter = ? AND subchapter = ?",
                   (username, chapter, subchapter))
    result = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    if result:
        result = [{'id': row[0], 'username': row[1], 'chapter': row[2], 'subchapter': row[3], 'score': row[4]}
                  for row in result]
    else:
        result = ''
    return jsonify(result)


@app.route('/searchTeacher', methods=['POST'])
def search_teacher():
    data = request.get_json()
    department = data.get('department')
    title = data.get('title')
    name = data.get('name')
    if department or title or name:
        # 修复：绝对路径连接数据库
        db_path = os.path.join(BASE_DIR, 'sqlite3db', 'dsavd.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        query = "SELECT * FROM teacher_profile WHERE 1=1"
        params = []
        if department:
            query += " AND department LIKE ?"
            params.append("%{}%".format(department))
        if title:
            query += " AND title LIKE ?"
            params.append("%{}%".format(title))
        if name:
            query += " AND name LIKE ?"
            params.append("%{}%".format(name))
        cursor.execute(query, params)
        result = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        if result:
            result = [{'id': row[0], 'college': row[1], 'department': row[2], 'title': row[3],
                       'name': row[4], 'avatar_url': row[5]} for row in result]
        else:
            result = ''
        return jsonify(result)


@app.route('/teacherList', methods=['POST'])
def teacher_list():
    # 修复：绝对路径连接数据库
    db_path = os.path.join(BASE_DIR, 'sqlite3db', 'dsavd.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM teacher_profile")
    result = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    if result:
        result = [{'id': row[0], 'college': row[1], 'department': row[2], 'title': row[3],
                   'name': row[4], 'avatar_url': row[5]} for row in result]
    else:
        result = ''
    return jsonify(result)



# =============================================
# 实时摄像头分析接口
# =============================================
import threading
import time

# 全局摄像头状态
camera_state = {
    'running': False,
    'cap': None,
    'emotion_count': {'专注': 0, '开心': 0, '惊讶': 0, '愤怒': 0, '无人脸': 0},
    'total_frames': 0,
    'attention_score': 0,
    'current_emotion': '',
    'face_count': 0,
}
camera_lock = threading.Lock()


def generate_camera_frames():
    """委托给 YOLO 实现，保持路由调用不变"""
    from camera_yolo import generate_camera_frames_yolo
    yield from generate_camera_frames_yolo(camera_state, camera_lock)


@app.route('/startCamera', methods=['POST'])
@teacher_only
def start_camera():
    with camera_lock:
        if camera_state['running']:
            return jsonify({'status': 'already_running'})
    return jsonify({'status': 'ok'})


@app.route('/videoFeed')
@teacher_only
def video_feed():
    return Response(
        generate_camera_frames(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )


@app.route('/stopCamera', methods=['POST'])
@teacher_only
def stop_camera():
    with camera_lock:
        camera_state['running'] = False
        if camera_state['cap']:
            camera_state['cap'].release()
            camera_state['cap'] = None

    # 计算最终专注度
    ec = camera_state['emotion_count']
    tf = camera_state['total_frames']
    face_frames = tf - ec['无人脸']
    attention_score = round(((ec['专注'] + ec['开心']) / face_frames) * 100, 1) if face_frames > 0 else 0

    return jsonify({
        'emotion_count': ec,
        'total_frames': tf,
        'attention_score': attention_score
    })


@app.route('/cameraStats')
@teacher_only
def camera_stats():
    with camera_lock:
        ec = dict(camera_state['emotion_count'])
        tf = camera_state['total_frames']
        score = camera_state['attention_score']
        emotion = camera_state['current_emotion']
        face_count = camera_state['face_count']
    return jsonify({
        'emotion_count': ec,
        'total_frames': tf,
        'attention_score': score,
        'current_emotion': emotion,
        'face_count': face_count,
    })


_deeptutor_process = None
_deeptutor_status = {'status': 'stopped', 'error': ''}


def _project_config():
    import yaml
    config_path = os.path.join(os.path.dirname(BASE_DIR), 'config.yaml')
    with open(config_path, encoding='utf-8') as config_file:
        config = yaml.load(config_file.read(), Loader=yaml.FullLoader)
    config['mysql']['password'] = os.environ.get('DSAVD_MYSQL_PASSWORD', config['mysql'].get('password', ''))
    return config


def _deeptutor_config():
    config = _project_config().get('integrations', {}).get('deeptutor', {})
    root = os.environ.get('DEEPTUTOR_ROOT', config.get('root', r'D:\bigchuang\DeepTutor-main\DeepTutor-main'))
    return {
        'root': os.path.abspath(root),
        'backend_port': int(config.get('backend_port', 8001)),
        'frontend_port': int(config.get('frontend_port', 3782)),
    }


def _port_is_open(port):
    import socket
    try:
        with socket.create_connection(('127.0.0.1', port), timeout=0.35):
            return True
    except OSError:
        return False


@app.route('/startDeepTutor', methods=['POST'])
def start_deeptutor():
    global _deeptutor_process, _deeptutor_status
    import subprocess
    import threading
    import time
    import shutil

    settings = _deeptutor_config()
    deeptutor_root = settings['root']
    venv_python = os.path.join(deeptutor_root, '.venv', 'Scripts', 'python.exe')
    frontend_port = settings['frontend_port']
    backend_port = settings['backend_port']
    frontend_url = '/deeptutor'

    if _port_is_open(frontend_port) and _port_is_open(backend_port):
        _deeptutor_status = {'status': 'running', 'error': ''}
        return jsonify({'status': 'running', 'frontend_url': frontend_url})
    if _deeptutor_status['status'] == 'starting':
        return jsonify({'status': 'starting', 'frontend_url': frontend_url})
    if not os.path.isfile(venv_python):
        return jsonify({'status': 'failed', 'error': f'DeepTutor Python 环境不存在: {venv_python}'}), 500
    if not os.path.isfile(os.path.join(deeptutor_root, 'web', 'package.json')):
        return jsonify({'status': 'failed', 'error': f'DeepTutor Web 目录无效: {deeptutor_root}'}), 500

    npm_executable = shutil.which('npm.cmd') or shutil.which('npm')
    if not npm_executable:
        return jsonify({'status': 'failed', 'error': '没有找到 npm，请先安装 Node.js。'}), 500

    _deeptutor_status = {'status': 'starting', 'error': ''}

    def run_deeptutor():
        global _deeptutor_process, _deeptutor_status
        try:
            process_flags = subprocess.CREATE_NEW_PROCESS_GROUP if os.name == 'nt' else 0
            backend_env = os.environ.copy()
            backend_env['PYTHONUNBUFFERED'] = '1'
            backend_env['PATH'] = os.path.join(deeptutor_root, '.venv', 'Scripts') + os.pathsep + backend_env.get('PATH', '')
            backend_process = subprocess.Popen(
                [venv_python, '-m', 'deeptutor.api.run_server'], cwd=deeptutor_root,
                env=backend_env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                creationflags=process_flags
            )
            time.sleep(3)
            if backend_process.poll() is not None:
                raise RuntimeError(f'DeepTutor 后端启动失败，退出码 {backend_process.returncode}')

            frontend_env = os.environ.copy()
            frontend_env['NEXT_PUBLIC_API_BASE'] = f'http://127.0.0.1:{backend_port}'
            frontend_process = subprocess.Popen(
                [npm_executable, 'run', 'dev', '--', '--port', str(frontend_port)],
                cwd=os.path.join(deeptutor_root, 'web'), env=frontend_env,
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, creationflags=process_flags
            )
            _deeptutor_process = {'backend': backend_process, 'frontend': frontend_process}
            _deeptutor_status = {'status': 'starting', 'error': ''}
            print(f'DeepTutor started: backend={backend_process.pid}, frontend={frontend_process.pid}')
        except Exception as error:
            _deeptutor_status = {'status': 'failed', 'error': str(error)}
            print(f'DeepTutor start failed: {error}')

    thread = threading.Thread(target=run_deeptutor, daemon=True)
    thread.start()

    return jsonify({'status': 'starting', 'frontend_url': frontend_url})


@app.route('/isDeepTutorRunning', methods=['GET'])
def is_deeptutor_running():
    global _deeptutor_status
    settings = _deeptutor_config()
    running = _port_is_open(settings['backend_port']) and _port_is_open(settings['frontend_port'])
    if running:
        _deeptutor_status = {'status': 'running', 'error': ''}
    elif _deeptutor_process:
        exited = [name for name, process in _deeptutor_process.items() if process.poll() is not None]
        if exited:
            _deeptutor_status = {'status': 'failed', 'error': f"DeepTutor 进程异常退出: {', '.join(exited)}"}
    status = 'running' if running else _deeptutor_status['status']
    return jsonify({
        'running': running,
        'status': status,
        'error': _deeptutor_status.get('error', ''),
        'frontend_url': '/deeptutor'
    })


# =============================================
# MySQL 数据库连接（学生学习行为分析）
# =============================================
def _get_mysql_connection():
    """获取 MySQL 数据库连接"""
    import pymysql
    config = _project_config()
    mysql_config = config['mysql']
    return pymysql.connect(
        host=mysql_config['host'],
        port=mysql_config['port'],
        user=mysql_config['user'],
        password=mysql_config['password'],
        database=mysql_config['database'],
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )


STUDENT_LEARNING_DIR = os.path.join(BASE_DIR, 'student_learning_clips')
os.makedirs(STUDENT_LEARNING_DIR, exist_ok=True)


@app.route('/analyzeStudentLearning', methods=['POST'])
def analyze_student_learning():
    """
    学生慕课学习行为分析接口
    接收前端采集的10秒摄像头视频片段，调用表情识别分析，结果写入 MySQL
    """
    import json as _json

    username = request.form.get('username', '')
    chapter = request.form.get('chapter', '')
    subchapter = request.form.get('subchapter', '')
    learning_duration = int(request.form.get('learning_duration', 0))
    video_file = request.files.get('video')

    if not username or not chapter or not subchapter or not video_file:
        return jsonify({'message': '参数不完整'}), 400

    filename = f"{username}_{chapter}_{subchapter}_{int(time.time())}.webm"
    filepath = os.path.join(STUDENT_LEARNING_DIR, filename)
    video_file.save(filepath)
    print(f"学生学习视频片段已保存: {filepath}")

    stats = {"emotion_count": {}, "attention_score": 0, "total_frames": 0}
    try:
        from face_emotion.face_emotion import face_emotion
        my_face = face_emotion(filepath, os.path.join(STUDENT_LEARNING_DIR, f"result_{filename}"))
        result = my_face.learning_face()
        if isinstance(result, dict):
            stats = result
    except Exception as e:
        print(f"学生学习行为分析错误: {e}")

    emotion_count_json = _json.dumps(stats.get('emotion_count', {}), ensure_ascii=False)
    attention_score = float(stats.get('attention_score', 0))
    total_frames = int(stats.get('total_frames', 0))
    is_distracted = 1 if attention_score < 40 else 0
    behavior_label = '疑似走神' if is_distracted else '正常学习'

    try:
        conn = _get_mysql_connection()
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO student_learning_behavior
                (username, chapter, subchapter, attention_score, is_distracted, behavior_label,
                 total_frames, emotion_count, video_filename, learning_duration)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                username,
                chapter,
                subchapter,
                attention_score,
                is_distracted,
                behavior_label,
                total_frames,
                emotion_count_json,
                filename,
                learning_duration
            ))
        conn.commit()
        conn.close()
        print(f"分析结果已写入 MySQL: {username} 第{chapter}章{subchapter}节 专注度{attention_score}")
    except Exception as e:
        print(f"写入 MySQL 失败: {e}")
        return jsonify({'message': f'数据库写入失败: {str(e)}'}), 500

    return jsonify({
        'status': 'success',
        'attention_score': attention_score,
        'is_distracted': bool(is_distracted),
        'behavior_label': behavior_label,
        'total_frames': total_frames,
        'emotion_count': stats.get('emotion_count', {})
    })


@app.route('/getStudentLearningRecords', methods=['POST'])
def get_student_learning_records():
    """查询学生学习行为分析记录"""
    data = request.get_json() or {}
    username = data.get('username', '')
    chapter = data.get('chapter', '')
    subchapter = data.get('subchapter', '')

    if not username:
        return jsonify({'message': '用户名不能为空'}), 400

    try:
        conn = _get_mysql_connection()
        with conn.cursor() as cursor:
            sql = "SELECT * FROM student_learning_behavior WHERE username = %s"
            params = [username]
            if chapter:
                sql += " AND chapter = %s"
                params.append(chapter)
            if subchapter:
                sql += " AND subchapter = %s"
                params.append(subchapter)
            sql += " ORDER BY created_time DESC LIMIT 100"
            cursor.execute(sql, params)
            records = cursor.fetchall()
        conn.close()

        import json as _json
        for record in records:
            if isinstance(record.get('emotion_count'), str):
                try:
                    record['emotion_count'] = _json.loads(record['emotion_count'])
                except Exception:
                    record['emotion_count'] = {}

        return jsonify(records)
    except Exception as e:
        print(f"查询 MySQL 失败: {e}")
        return jsonify({'message': f'数据库查询失败: {str(e)}'}), 500


# =============================================
# 答题防作弊：摄像头截图上传、AI手机检测与查询
# =============================================
_exam_ai_model = None


def _analyze_exam_snapshot(image_bytes):
    """使用本地 YOLO 模型检测答题画面中的手机，结果仅用于风险初筛。"""
    global _exam_ai_model
    import numpy as np
    import cv2
    from ultralytics import YOLO

    if _exam_ai_model is None:
        _exam_ai_model = YOLO(os.path.join(BASE_DIR, 'yolo11n.pt'))

    image = cv2.imdecode(np.frombuffer(image_bytes, dtype=np.uint8), cv2.IMREAD_COLOR)
    if image is None:
        raise ValueError('无法解析答题截图')

    result = _exam_ai_model.predict(image, conf=0.25, imgsz=640, verbose=False)[0]
    names = result.names
    phone_confidences = []
    person_count = 0
    for box in result.boxes:
        class_id = int(box.cls[0].item())
        confidence = float(box.conf[0].item())
        label = str(names.get(class_id, '')).lower()
        if label == 'person':
            person_count += 1
        if label in {'cell phone', 'mobile phone', 'phone'}:
            phone_confidences.append(confidence)

    phone_confidence = max(phone_confidences, default=0.0)
    phone_detected = bool(phone_confidences)
    if phone_detected:
        reason = f'画面检测到手机，置信度 {phone_confidence:.1%}，疑似使用手机拍照搜题'
        status = 'suspected'
    else:
        reason = '未检测到手机物体'
        status = 'normal'
    return {
        'ai_status': status,
        'phone_detected': int(phone_detected),
        'phone_confidence': phone_confidence,
        'person_count': person_count,
        'ai_reason': reason,
    }


@app.route('/uploadExamSnapshot', methods=['POST'])
def upload_exam_snapshot():
    """
    接收答题期间每3分钟采集的摄像头截图（JPEG）。
    数据库只保留该用户最近 30 张截图。
    """
    import base64

    username = request.form.get('username', '')
    chapter = request.form.get('chapter', '')
    subchapter = request.form.get('subchapter', '')
    image_file = request.files.get('image')

    if not username or not image_file:
        return jsonify({'message': '参数不完整'}), 400

    image_bytes = image_file.read()
    image_b64 = base64.b64encode(image_bytes).decode('utf-8')
    filename = f"{username}_{chapter}_{subchapter}_{int(time.time())}.jpg"
    try:
        ai_result = _analyze_exam_snapshot(image_bytes)
    except Exception as ai_error:
        print(f'答题截图 AI 分析失败: {ai_error}')
        ai_result = {
            'ai_status': 'error', 'phone_detected': 0, 'phone_confidence': 0,
            'person_count': 0, 'ai_reason': f'AI分析失败: {ai_error}'
        }

    try:
        conn = _get_mysql_connection()
        with conn.cursor() as cursor:
            # 插入新截图
            insert_sql = """
                INSERT INTO exam_monitor_snapshot
                (username, chapter, subchapter, image_base64, image_filename,
                 ai_status, phone_detected, phone_confidence, person_count, ai_reason, analyzed_time)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())
            """
            cursor.execute(insert_sql, (
                username, chapter, subchapter, image_b64, filename,
                ai_result['ai_status'], ai_result['phone_detected'], ai_result['phone_confidence'],
                ai_result['person_count'], ai_result['ai_reason']
            ))

            # 仅保留最近 30 张：删除多余的旧记录
            cursor.execute(
                "SELECT COUNT(*) AS cnt FROM exam_monitor_snapshot WHERE username = %s",
                (username,)
            )
            total = cursor.fetchone()['cnt']
            if total > 30:
                delete_sql = """
                    DELETE FROM exam_monitor_snapshot
                    WHERE username = %s
                      AND id NOT IN (
                          SELECT id FROM (
                              SELECT id FROM exam_monitor_snapshot
                              WHERE username = %s
                              ORDER BY created_time DESC
                              LIMIT 30
                          ) AS keep_ids
                      )
                """
                cursor.execute(delete_sql, (username, username))
        conn.commit()
        conn.close()
        print(f"答题截图已保存: {filename} (用户 {username} 当前共保留<=30张)")
        return jsonify({'status': 'success', 'image_filename': filename, 'ai_result': ai_result})
    except Exception as e:
        print(f"保存答题截图失败: {e}")
        return jsonify({'message': f'保存失败: {str(e)}'}), 500


@app.route('/getExamSnapshots', methods=['POST'])
def get_exam_snapshots():
    """查询某用户最近 30 张答题截图（仅返回元信息和 base64，供前端展示）"""
    data = request.get_json() or {}
    username = data.get('username', '')
    if not username:
        return jsonify({'message': '用户名不能为空'}), 400

    try:
        conn = _get_mysql_connection()
        with conn.cursor() as cursor:
            sql = """
                SELECT id, username, chapter, subchapter, image_filename, created_time, image_base64,
                       ai_status, phone_detected, phone_confidence, person_count, ai_reason, analyzed_time
                FROM exam_monitor_snapshot
                WHERE username = %s
                ORDER BY created_time DESC
                LIMIT 30
            """
            cursor.execute(sql, (username,))
            records = cursor.fetchall()
        conn.close()
        return jsonify(records)
    except Exception as e:
        print(f"查询答题截图失败: {e}")
        return jsonify({'message': f'查询失败: {str(e)}'}), 500


# =============================================
# 智慧教室：慕课学习监测与答题行为监管
# =============================================
@app.route('/learning/monitor', methods=['GET'])
@teacher_only
def learning_monitor():
    username = request.args.get('username', '').strip()
    chapter = request.args.get('chapter', '').strip()
    page_num = max(1, int(request.args.get('pageNum', 1)))
    page_size = min(100, max(1, int(request.args.get('pageSize', 20))))
    where = ['1=1']
    params = []
    if username:
        where.append('username LIKE %s')
        params.append(f'%{username}%')
    if chapter:
        where.append('chapter = %s')
        params.append(chapter)
    where_sql = ' AND '.join(where)

    try:
        conn = _get_mysql_connection()
        with conn.cursor() as cursor:
            cursor.execute(f"""
                SELECT COUNT(*) AS total FROM (
                    SELECT username, chapter, subchapter, DATE(created_time)
                    FROM student_learning_behavior WHERE {where_sql}
                    GROUP BY username, chapter, subchapter, DATE(created_time)
                ) grouped_records
            """, params)
            total = cursor.fetchone()['total']
            cursor.execute(f"""
                SELECT username, chapter, subchapter, DATE(created_time) AS learning_date,
                       MAX(learning_duration) AS learning_duration,
                       ROUND(AVG(attention_score), 1) AS attention_score,
                       SUM(is_distracted) AS distracted_samples,
                       COUNT(*) AS sample_count,
                       MAX(created_time) AS last_learning_time
                FROM student_learning_behavior
                WHERE {where_sql}
                GROUP BY username, chapter, subchapter, DATE(created_time)
                ORDER BY last_learning_time DESC
                LIMIT %s OFFSET %s
            """, params + [page_size, (page_num - 1) * page_size])
            rows = cursor.fetchall()
            cursor.execute(f"""
                SELECT COUNT(DISTINCT username) AS student_count,
                       COALESCE(SUM(daily_duration), 0) AS total_duration,
                       ROUND(COALESCE(AVG(avg_attention), 0), 1) AS avg_attention,
                       COALESCE(SUM(distracted_count), 0) AS distracted_count
                FROM (
                    SELECT username, chapter, subchapter, DATE(created_time),
                           MAX(learning_duration) AS daily_duration,
                           AVG(attention_score) AS avg_attention,
                           SUM(is_distracted) AS distracted_count
                    FROM student_learning_behavior WHERE {where_sql}
                    GROUP BY username, chapter, subchapter, DATE(created_time)
                ) summary_rows
            """, params)
            summary = cursor.fetchone()
        conn.close()
        for row in rows:
            row['is_distracted'] = bool(row['distracted_samples']) or float(row['attention_score'] or 0) < 40
            row['behavior_label'] = '疑似走神' if row['is_distracted'] else '正常学习'
        return jsonify({'code': 200, 'total': total, 'rows': rows, 'summary': summary})
    except Exception as error:
        return jsonify({'code': 500, 'message': str(error)}), 500


@app.route('/learning/progress', methods=['POST'])
def update_learning_progress():
    """视频暂停或离开时刷新当前章节的实际累计观看时长。"""
    data = request.get_json() or {}
    username = data.get('username', '')
    chapter = data.get('chapter', '')
    subchapter = data.get('subchapter', '')
    duration = max(0, int(data.get('learningDuration', 0)))
    if not username or not chapter or not subchapter:
        return jsonify({'message': '参数不完整'}), 400
    try:
        conn = _get_mysql_connection()
        with conn.cursor() as cursor:
            cursor.execute("""
                UPDATE student_learning_behavior
                SET learning_duration = GREATEST(learning_duration, %s)
                WHERE id = (
                    SELECT id FROM (
                        SELECT id FROM student_learning_behavior
                        WHERE username=%s AND chapter=%s AND subchapter=%s
                        ORDER BY created_time DESC LIMIT 1
                    ) latest_record
                )
            """, (duration, username, chapter, subchapter))
        conn.commit()
        conn.close()
        return jsonify({'status': 'success'})
    except Exception as error:
        return jsonify({'message': str(error)}), 500


@app.route('/exam/behavior/event', methods=['POST'])
def record_exam_behavior_event():
    data = request.get_json() or {}
    required = ('username', 'eventType')
    if any(not data.get(key) for key in required):
        return jsonify({'message': '参数不完整'}), 400
    try:
        conn = _get_mysql_connection()
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO exam_behavior_event
                (username, chapter, subchapter, event_type, event_detail)
                VALUES (%s, %s, %s, %s, %s)
            """, (
                data['username'], data.get('chapter', ''), data.get('subchapter', ''),
                data['eventType'], data.get('eventDetail', '')
            ))
        conn.commit()
        conn.close()
        return jsonify({'status': 'success'})
    except Exception as error:
        return jsonify({'message': str(error)}), 500


@app.route('/exam/monitor', methods=['GET'])
@teacher_only
def exam_monitor():
    username = request.args.get('username', '').strip()
    chapter = request.args.get('chapter', '').strip()
    page_num = max(1, int(request.args.get('pageNum', 1)))
    page_size = min(100, max(1, int(request.args.get('pageSize', 20))))
    filters = []
    params = []
    if username:
        filters.append('keys_table.username LIKE %s')
        params.append(f'%{username}%')
    if chapter:
        filters.append('keys_table.chapter = %s')
        params.append(chapter)
    where_sql = ('WHERE ' + ' AND '.join(filters)) if filters else ''
    try:
        conn = _get_mysql_connection()
        with conn.cursor() as cursor:
            key_sql = """
                SELECT username, chapter, subchapter FROM exam_answer_record
                UNION SELECT username, chapter, subchapter FROM exam_behavior_event
                UNION SELECT username, chapter, subchapter FROM exam_monitor_snapshot
            """
            cursor.execute(f"SELECT COUNT(*) AS total FROM ({key_sql}) keys_table {where_sql}", params)
            total = cursor.fetchone()['total']
            cursor.execute(f"""
                SELECT keys_table.username, keys_table.chapter, keys_table.subchapter,
                       answers.score, answers.updated_time,
                       COALESCE(events.event_count, 0) AS event_count,
                       COALESCE(shots.snapshot_count, 0) AS snapshot_count,
                       COALESCE(shots.suspected_count, 0) AS suspected_count,
                       COALESCE(shots.max_phone_confidence, 0) AS max_phone_confidence,
                       GREATEST(COALESCE(answers.updated_time, '1970-01-01'),
                                COALESCE(events.last_event_time, '1970-01-01'),
                                COALESCE(shots.last_snapshot_time, '1970-01-01')) AS last_activity_time
                FROM ({key_sql}) keys_table
                LEFT JOIN exam_answer_record answers
                  ON answers.username=keys_table.username AND answers.chapter=keys_table.chapter AND answers.subchapter=keys_table.subchapter
                LEFT JOIN (
                    SELECT username, chapter, subchapter, COUNT(*) event_count, MAX(occurred_time) last_event_time
                    FROM exam_behavior_event GROUP BY username, chapter, subchapter
                ) events ON events.username=keys_table.username AND events.chapter=keys_table.chapter AND events.subchapter=keys_table.subchapter
                LEFT JOIN (
                    SELECT username, chapter, subchapter, COUNT(*) snapshot_count,
                           SUM(phone_detected) suspected_count, MAX(phone_confidence) max_phone_confidence,
                           MAX(created_time) last_snapshot_time
                    FROM exam_monitor_snapshot GROUP BY username, chapter, subchapter
                ) shots ON shots.username=keys_table.username AND shots.chapter=keys_table.chapter AND shots.subchapter=keys_table.subchapter
                {where_sql}
                ORDER BY last_activity_time DESC
                LIMIT %s OFFSET %s
            """, params + [page_size, (page_num - 1) * page_size])
            rows = cursor.fetchall()
            cursor.execute("""
                SELECT COUNT(DISTINCT username) student_count,
                       COUNT(*) snapshot_count,
                       COALESCE(SUM(phone_detected), 0) suspected_count
                FROM exam_monitor_snapshot
            """)
            shot_summary = cursor.fetchone()
            cursor.execute("SELECT COUNT(*) AS event_count FROM exam_behavior_event")
            event_count = cursor.fetchone()['event_count']
        conn.close()
        for row in rows:
            row['risk_level'] = 'high' if row['suspected_count'] else ('medium' if row['event_count'] else 'normal')
        return jsonify({'code': 200, 'total': total, 'rows': rows, 'summary': {**shot_summary, 'event_count': event_count}})
    except Exception as error:
        return jsonify({'code': 500, 'message': str(error)}), 500


@app.route('/exam/monitor/detail', methods=['GET'])
@teacher_only
def exam_monitor_detail():
    username = request.args.get('username', '')
    chapter = request.args.get('chapter', '')
    subchapter = request.args.get('subchapter', '')
    params = (username, chapter, subchapter)
    try:
        conn = _get_mysql_connection()
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT id, event_type, event_detail, occurred_time FROM exam_behavior_event
                WHERE username=%s AND chapter=%s AND subchapter=%s ORDER BY occurred_time DESC LIMIT 100
            """, params)
            events = cursor.fetchall()
            cursor.execute("""
                SELECT id, image_base64, image_filename, ai_status, phone_detected,
                       phone_confidence, person_count, ai_reason, created_time, analyzed_time
                FROM exam_monitor_snapshot
                WHERE username=%s AND chapter=%s AND subchapter=%s ORDER BY created_time DESC LIMIT 30
            """, params)
            snapshots = cursor.fetchall()
        conn.close()
        return jsonify({'events': events, 'snapshots': snapshots})
    except Exception as error:
        return jsonify({'message': str(error)}), 500


# =============================================
# 智慧教室 API 路由
# =============================================

# ---------- 巡查点管理 ----------
@app.route('/rsm/patrol/point/list', methods=['GET'])
def list_patrol_point():
    """查询巡查点列表"""
    query = request.args.to_dict()
    patrol_name = query.get('patrolName', '')
    position = query.get('position', '')
    security_officer = query.get('securityOfficer', '')
    status = query.get('status', '')
    page_num = int(query.get('pageNum', 1))
    page_size = int(query.get('pageSize', 10))
    try:
        conn = _get_mysql_connection()
        with conn.cursor() as cursor:
            where = "WHERE del_flag = 0"
            params = []
            if patrol_name:
                where += " AND patrol_name LIKE %s"
                params.append(f"%{patrol_name}%")
            if position:
                where += " AND position LIKE %s"
                params.append(f"%{position}%")
            if security_officer:
                where += " AND security_officer LIKE %s"
                params.append(f"%{security_officer}%")
            if status:
                where += " AND status = %s"
                params.append(status)
            cursor.execute(f"SELECT COUNT(*) as total FROM rsm_patrol_point {where}", params)
            total = cursor.fetchone()['total']
            offset = (page_num - 1) * page_size
            cursor.execute(
                f"SELECT * FROM rsm_patrol_point {where} ORDER BY create_time DESC LIMIT %s OFFSET %s",
                params + [page_size, offset]
            )
            rows = cursor.fetchall()
        conn.close()
        return jsonify({'total': total, 'rows': rows, 'code': 200})
    except Exception as e:
        return jsonify({'message': str(e), 'code': 500}), 500


@app.route('/rsm/patrol/point/<int:point_id>', methods=['GET'])
def get_patrol_point(point_id):
    """查询巡查点详情"""
    try:
        conn = _get_mysql_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM rsm_patrol_point WHERE id = %s AND del_flag = 0", (point_id,))
            row = cursor.fetchone()
        conn.close()
        return jsonify(row or {})
    except Exception as e:
        return jsonify({'message': str(e)}), 500


@app.route('/rsm/patrol/point', methods=['POST'])
def add_patrol_point():
    """新增巡查点"""
    data = request.get_json() or {}
    try:
        conn = _get_mysql_connection()
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO rsm_patrol_point
                (patrol_name, patrol_desc, position, location_describe, security_officer, status, remark)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                data.get('patrolName', ''),
                data.get('patrolDesc', ''),
                data.get('position', ''),
                data.get('locationDescribe', ''),
                data.get('securityOfficer', ''),
                data.get('status', 0),
                data.get('remark', '')
            ))
        conn.commit()
        conn.close()
        return jsonify({'code': 200, 'msg': '新增成功'})
    except Exception as e:
        return jsonify({'code': 500, 'msg': str(e)}), 500


@app.route('/rsm/patrol/point', methods=['PUT'])
def update_patrol_point():
    """修改巡查点"""
    data = request.get_json() or {}
    try:
        conn = _get_mysql_connection()
        with conn.cursor() as cursor:
            sql = """
                UPDATE rsm_patrol_point SET
                patrol_name=%s, patrol_desc=%s, position=%s, location_describe=%s,
                security_officer=%s, status=%s, remark=%s
                WHERE id=%s
            """
            cursor.execute(sql, (
                data.get('patrolName', ''),
                data.get('patrolDesc', ''),
                data.get('position', ''),
                data.get('locationDescribe', ''),
                data.get('securityOfficer', ''),
                data.get('status', 0),
                data.get('remark', ''),
                data.get('id')
            ))
        conn.commit()
        conn.close()
        return jsonify({'code': 200, 'msg': '修改成功'})
    except Exception as e:
        return jsonify({'code': 500, 'msg': str(e)}), 500


@app.route('/rsm/patrol/point/<int:point_id>', methods=['DELETE'])
def del_patrol_point(point_id):
    """删除巡查点（逻辑删除）"""
    try:
        conn = _get_mysql_connection()
        with conn.cursor() as cursor:
            cursor.execute("UPDATE rsm_patrol_point SET del_flag = 1 WHERE id = %s", (point_id,))
        conn.commit()
        conn.close()
        return jsonify({'code': 200, 'msg': '删除成功'})
    except Exception as e:
        return jsonify({'code': 500, 'msg': str(e)}), 500


# ---------- 巡查清单 ----------
@app.route('/rsm/patrol/list/list', methods=['GET'])
def list_patrol_list():
    """查询巡查清单列表"""
    query = request.args.to_dict()
    patrol_list_name = query.get('patrolListName', '')
    status = query.get('status', '')
    page_num = int(query.get('pageNum', 1))
    page_size = int(query.get('pageSize', 10))
    try:
        conn = _get_mysql_connection()
        with conn.cursor() as cursor:
            where = "WHERE del_flag = 0"
            params = []
            if patrol_list_name:
                where += " AND patrol_list_name LIKE %s"
                params.append(f"%{patrol_list_name}%")
            if status:
                where += " AND status = %s"
                params.append(status)
            cursor.execute(f"SELECT COUNT(*) as total FROM rsm_patrol_list {where}", params)
            total = cursor.fetchone()['total']
            offset = (page_num - 1) * page_size
            cursor.execute(
                f"SELECT * FROM rsm_patrol_list {where} ORDER BY create_time DESC LIMIT %s OFFSET %s",
                params + [page_size, offset]
            )
            rows = cursor.fetchall()
        conn.close()
        return jsonify({'total': total, 'rows': rows, 'code': 200})
    except Exception as e:
        return jsonify({'message': str(e), 'code': 500}), 500


@app.route('/rsm/patrol/list', methods=['POST'])
def add_patrol_list():
    """新增巡查清单"""
    data = request.get_json() or {}
    try:
        conn = _get_mysql_connection()
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO rsm_patrol_list
                (patrol_list_name, principal_id, start_time, end_time, waiting_checked, status, remark)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                data.get('patrolListName', ''),
                data.get('principalId'),
                data.get('startTime'),
                data.get('endTime'),
                data.get('waitingChecked', 0),
                data.get('status', 0),
                data.get('remark', '')
            ))
        conn.commit()
        conn.close()
        return jsonify({'code': 200, 'msg': '新增成功'})
    except Exception as e:
        return jsonify({'code': 500, 'msg': str(e)}), 500


@app.route('/rsm/patrol/list', methods=['PUT'])
def update_patrol_list():
    """修改巡查清单"""
    data = request.get_json() or {}
    try:
        conn = _get_mysql_connection()
        with conn.cursor() as cursor:
            sql = """
                UPDATE rsm_patrol_list SET
                patrol_list_name=%s, principal_id=%s, start_time=%s, end_time=%s,
                waiting_checked=%s, checked_count=%s, hidden_trouble_count=%s,
                finish_time=%s, status=%s, remark=%s
                WHERE id=%s
            """
            cursor.execute(sql, (
                data.get('patrolListName', ''),
                data.get('principalId'),
                data.get('startTime'),
                data.get('endTime'),
                data.get('waitingChecked', 0),
                data.get('checkedCount', 0),
                data.get('hiddenTroubleCount', 0),
                data.get('finishTime'),
                data.get('status', 0),
                data.get('remark', ''),
                data.get('id')
            ))
        conn.commit()
        conn.close()
        return jsonify({'code': 200, 'msg': '修改成功'})
    except Exception as e:
        return jsonify({'code': 500, 'msg': str(e)}), 500


@app.route('/rsm/patrol/list/<int:list_id>', methods=['DELETE'])
def del_patrol_list(list_id):
    """删除巡查清单"""
    try:
        conn = _get_mysql_connection()
        with conn.cursor() as cursor:
            cursor.execute("UPDATE rsm_patrol_list SET del_flag = 1 WHERE id = %s", (list_id,))
        conn.commit()
        conn.close()
        return jsonify({'code': 200, 'msg': '删除成功'})
    except Exception as e:
        return jsonify({'code': 500, 'msg': str(e)}), 500


# ---------- 随手拍问题 ----------
@app.route('/rsm/snapshot/list', methods=['GET'])
def list_snapshot():
    """查询随手拍问题列表"""
    query = request.args.to_dict()
    question_title = query.get('questionTitle', '')
    property_val = query.get('property', '')
    page_num = int(query.get('pageNum', 1))
    page_size = int(query.get('pageSize', 10))
    try:
        conn = _get_mysql_connection()
        with conn.cursor() as cursor:
            where = "WHERE 1=1"
            params = []
            if question_title:
                where += " AND question_title LIKE %s"
                params.append(f"%{question_title}%")
            if property_val:
                where += " AND property = %s"
                params.append(property_val)
            cursor.execute(f"SELECT COUNT(*) as total FROM rsm_snapshot {where}", params)
            total = cursor.fetchone()['total']
            offset = (page_num - 1) * page_size
            cursor.execute(
                f"SELECT * FROM rsm_snapshot {where} ORDER BY create_time DESC LIMIT %s OFFSET %s",
                params + [page_size, offset]
            )
            rows = cursor.fetchall()
        conn.close()
        return jsonify({'total': total, 'rows': rows, 'code': 200})
    except Exception as e:
        return jsonify({'message': str(e), 'code': 500}), 500


@app.route('/rsm/snapshot/<int:snapshot_id>', methods=['GET'])
def get_snapshot(snapshot_id):
    """查询随手拍详情"""
    try:
        conn = _get_mysql_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM rsm_snapshot WHERE id = %s", (snapshot_id,))
            row = cursor.fetchone()
        conn.close()
        return jsonify(row or {})
    except Exception as e:
        return jsonify({'message': str(e)}), 500


@app.route('/rsm/snapshot', methods=['POST'])
def add_snapshot():
    """新增随手拍问题"""
    data = request.get_json() or {}
    try:
        conn = _get_mysql_connection()
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO rsm_snapshot
                (question_title, question_desc, creator_id, img_path, property, remark)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                data.get('questionTitle', ''),
                data.get('questionDesc', ''),
                data.get('creatorId'),
                data.get('imgPath', ''),
                data.get('property', 0),
                data.get('remark', '')
            ))
        conn.commit()
        conn.close()
        return jsonify({'code': 200, 'msg': '新增成功'})
    except Exception as e:
        return jsonify({'code': 500, 'msg': str(e)}), 500


@app.route('/rsm/snapshot', methods=['PUT'])
def update_snapshot():
    """修改随手拍问题 / 审批"""
    data = request.get_json() or {}
    try:
        conn = _get_mysql_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM rsm_snapshot WHERE id = %s", (data.get('id'),))
            current = cursor.fetchone()
            if not current:
                conn.close()
                return jsonify({'code': 404, 'msg': '问题记录不存在'}), 404
            sql = """
                UPDATE rsm_snapshot SET
                question_title=%s, question_desc=%s, img_path=%s,
                handler_id=%s, approval_reply=%s, property=%s, handler_time=%s, remark=%s
                WHERE id=%s
            """
            cursor.execute(sql, (
                data.get('questionTitle', current['question_title']),
                data.get('questionDesc', current['question_desc']),
                data.get('imgPath', current['img_path']),
                data.get('handlerId', current['handler_id']),
                data.get('approvalReply', current['approval_reply']),
                data.get('property', current['property']),
                data.get('handlerTime', current['handler_time']),
                data.get('remark', current['remark']),
                data.get('id')
            ))
        conn.commit()
        conn.close()
        return jsonify({'code': 200, 'msg': '修改成功'})
    except Exception as e:
        return jsonify({'code': 500, 'msg': str(e)}), 500


@app.route('/rsm/snapshot/<int:snapshot_id>', methods=['DELETE'])
def del_snapshot(snapshot_id):
    """删除随手拍问题"""
    try:
        conn = _get_mysql_connection()
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM rsm_snapshot WHERE id = %s", (snapshot_id,))
        conn.commit()
        conn.close()
        return jsonify({'code': 200, 'msg': '删除成功'})
    except Exception as e:
        return jsonify({'code': 500, 'msg': str(e)}), 500


# ---------- 3D教室仿真（PyBullet 独立进程 127.0.0.1:3100） ----------
CLASSROOM_SIM_URL = os.environ.get('CLASSROOM_SIM_URL', 'http://127.0.0.1:3100/api/sim')


def _classroom_sim(path, method='GET', payload=None, timeout=15):
    """把主服务请求转发给 PyBullet 仿真进程，原样返回结果。"""
    url = CLASSROOM_SIM_URL + path
    data = None
    headers = {}
    if payload is not None:
        data = json.dumps(payload).encode('utf-8')
        headers['Content-Type'] = 'application/json'
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            content_type = resp.headers.get('Content-Type', 'application/json')
            return Response(resp.read(), status=resp.status,
                            mimetype=content_type.split(';')[0].strip())
    except urllib.error.HTTPError as exc:
        try:
            parsed = json.loads(exc.read().decode('utf-8'))
        except Exception:
            parsed = {'ok': False, 'error': '仿真服务返回错误'}
        return jsonify(parsed), exc.code
    except Exception as exc:
        return jsonify({'ok': False, 'error': f'仿真服务不可用: {exc}'}), 503


@app.route('/rsm/classroom/sim/health', methods=['GET'])
def classroom_sim_health():
    return _classroom_sim('/health', timeout=5)


@app.route('/rsm/classroom/sim/info', methods=['GET'])
def classroom_sim_info():
    return _classroom_sim('/info')


@app.route('/rsm/classroom/sim/state', methods=['GET'])
def classroom_sim_state():
    return _classroom_sim('/state', timeout=8)


@app.route('/rsm/classroom/sim/plan', methods=['POST'])
def classroom_sim_plan():
    return _classroom_sim('/plan', 'POST', request.get_json(silent=True) or {})


@app.route('/rsm/classroom/sim/start', methods=['POST'])
def classroom_sim_start():
    return _classroom_sim('/start', 'POST', {})


@app.route('/rsm/classroom/sim/stop', methods=['POST'])
def classroom_sim_stop():
    return _classroom_sim('/stop', 'POST', {})


@app.route('/rsm/classroom/sim/reset', methods=['POST'])
def classroom_sim_reset():
    return _classroom_sim('/reset', 'POST', {})


@app.route('/rsm/classroom/sim/teleop', methods=['POST'])
def classroom_sim_teleop():
    return _classroom_sim('/teleop', 'POST', request.get_json(silent=True) or {})


@app.route('/rsm/classroom/sim/obstacle', methods=['POST'])
def classroom_sim_obstacle():
    return _classroom_sim('/obstacle', 'POST', request.get_json(silent=True) or {})


@app.route('/rsm/classroom/sim/obstacles/clear', methods=['POST'])
def classroom_sim_clear_obstacles():
    return _classroom_sim('/obstacles/clear', 'POST', {})


@app.route('/rsm/classroom/sim/camera.jpg', methods=['GET'])
def classroom_sim_camera():
    return _classroom_sim('/camera.jpg', timeout=30)


if __name__ == '__main__':
    import yaml

    # 修复：绝对路径读取config.yaml
    config_path = os.path.join(os.path.dirname(BASE_DIR), 'config.yaml')
    with open(config_path, encoding='utf-8') as file:  # 新增：指定编码，避免中文乱码
        config = yaml.load(file.read(), Loader=yaml.FullLoader)
    app.run(host=config["host"]["backend"], port=config["port"]["backend"], debug=True)
