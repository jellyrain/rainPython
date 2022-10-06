# ffmpeg 路径
FFMPEG_PATH = r'vacc\FF\ffmpeg.exe'


# 预设类
class Preset:
    def __init__(self, name: str, video: str, audio: str):
        self.format = name
        self.video = video
        self.audio = audio


# mp4 预设
mp4 = Preset('mp4', 'h264', 'acc')

# webm 预设
webm = Preset('webm', 'vp8', 'vorbis')

# ogg 预设
ogg = Preset('ogg', 'theora', 'vorbis')
