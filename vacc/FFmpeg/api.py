import os

from vacc.FFmpeg.config import FFMPEG_PATH, Preset


class Video:
    def __init__(self, path: str = FFMPEG_PATH) -> None:
        self.__path = path
        self.__input_file = None

    def input_file(self, file: str) -> 'Video':
        """输入文件"""
        self.__input_file = file
        return self

    def __is_input_file(self) -> None:
        """是否有输入文件"""
        if self.input_file is None:
            raise Exception('输入文件没有进行设置')

    def output_simple(self, file_name: str, file_format: str) -> str:
        """简单转换"""
        self.__is_input_file()
        return os.popen(f'{self.__path} -i {self.__input_file} -c copy {file_name}.{file_format}').read()

    def output_video_only(self, file_name: str, file_format: str) -> str:
        """只输出视频 注意：不需要加后缀"""
        self.__is_input_file()
        return os.popen(f'{self.__path} -i {self.__input_file} -c:v copy -an {file_name}.{file_format}').read()

    def output_audio_only(self, file_name: str, file_format: str) -> str:
        """只输出音频 注意：不需要加后缀"""
        self.__is_input_file()
        return os.popen(f'{self.__path} -i {self.__input_file} -f {file_format} -vn {file_name}.{file_format}').read()

    def insert_logo_video(self, file_name: str, file_format: str, img_path: str, x: int, y: int) -> str:
        """输出插入logo的视频"""
        self.__is_input_file()
        return os.popen(f'{self.__path} -i {self.__input_file} -i {img_path} -filter_complex overlay={x}:{y} {file_name}.{file_format}').read()

    def set_video_multiplier(self, file_name: str, file_format: str, multiplier: float) -> str:
        """设置视频播放速度并输出 调整速度倍率范围[0.25, 4]"""
        self.__is_input_file()
        return os.popen(f'{self.__path} -i {self.__input_file} -vf "setpts={1 / multiplier}*PTS" -af "atempo={multiplier}" {file_name}.{file_format}').read()

    def output_preset_file(self, file_name: str, preset: Preset) -> str:
        """输出预设格式文件"""
        self.__is_input_file()
        return os.popen(f'{self.__path} -i {self.__input_file} -c:v {preset.video} -c:a {preset.audio} {file_name}.{preset.format}').read()

    def modify_video_resolution(self, file_name: str, file_format: str, width: int, height: int = -1, setdar: str = '16:9') -> str:
        """修改视频分辨率和纵横比"""
        self.__is_input_file()
        return os.popen(f'{self.__path} -i {self.__input_file} -vf "scale={width}:{height} setdar={setdar}" {file_name}.{file_format}').read()