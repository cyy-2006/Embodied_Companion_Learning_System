import os

os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
os.environ.setdefault("HF_HUB_DISABLE_XET", "1")
import ctranslate2
from faster_whisper import WhisperModel
from moviepy.editor import VideoFileClip


class voice_recognition:
    def __init__(self,input_video):
        self.input_video = input_video

    def speech_to_text(self):
        model_size = os.environ.get("DSAVD_WHISPER_MODEL", "small")
        has_cuda = ctranslate2.get_cuda_device_count() > 0
        device = "cuda" if has_cuda else "cpu"
        compute_type = "float16" if has_cuda else "int8"

        model = WhisperModel(model_size, device=device, compute_type=compute_type)

        video = VideoFileClip(self.input_video)
        audio_path = "out.wav"
        video.audio.write_audiofile(audio_path)

        # segments, info = model.transcribe("audio.mp3", beam_size=5)
        segments, info = model.transcribe("out.wav", beam_size=5)

        print("Detected language '%s' with probability %f" % (info.language, info.language_probability))


        time=[]
        text=[]

        for segment in segments:
            # print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
            time.append("%.2fs -> %.2fs" % (segment.start, segment.end))
            text.append(segment.text)

        return time, text
#
if __name__ == '__main__':
    print(voice_recognition("2.mp4").speech_to_text())
