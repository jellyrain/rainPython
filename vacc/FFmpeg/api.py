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

    def output_subtitles_only(self, file_name: str, file_format: str) -> str:
        """输出字幕文件"""
        self.__is_input_file()
        return os.popen(f'{self.__path} -i {self.__input_file} -vn -an -c:s copy {file_name}.{file_format}').read()

    def insert_logo(self, file_name: str, file_format: str, img_path: str, x: int, y: int) -> str:
        """输出插入logo的视频"""
        self.__is_input_file()
        return os.popen(
            f'{self.__path} -i {self.__input_file} -i {img_path} -filter_complex overlay={x}:{y} {file_name}.{file_format}').read()

    def set_video_multiplier(self, file_name: str, file_format: str, multiplier: float) -> str:
        """设置视频播放速度并输出 调整速度倍率范围[0.25, 4]"""
        self.__is_input_file()
        return os.popen(
            f'{self.__path} -i {self.__input_file} -vf "setpts={1 / multiplier}*PTS" -af "atempo={multiplier}" {file_name}.{file_format}').read()

    def output_preset_file(self, file_name: str, preset: Preset) -> str:
        """输出预设格式文件"""
        self.__is_input_file()
        return os.popen(
            f'{self.__path} -i {self.__input_file} -c:v {preset.video} -c:a {preset.audio} {file_name}.{preset.format}').read()

    def modify_video_resolution(self, file_name: str, file_format: str, width: int, height: int = -1,
                                setdar: str = '16:9') -> str:
        """修改视频分辨率和纵横比"""
        self.__is_input_file()
        return os.popen(
            f'{self.__path} -i {self.__input_file} -vf "scale={width}:{height} setdar={setdar}" {file_name}.{file_format}').read()

    def modify_video_frame_rate(self, file_name: str, file_format: str, fps: int) -> str:
        """修改视频帧率"""
        self.__is_input_file()
        return os.popen(f'{self.__path} -i {self.__input_file} -r {fps} {file_name}.{file_format}').read()

    def modify_video_bitrate(self, file_name: str, file_format: str, bitrate: int) -> str:
        """修改视频码率"""
        self.__is_input_file()
        return os.popen(f'{self.__path} -i {self.__input_file} -b:v {bitrate}k {file_name}.{file_format}').read()

    def crop_video_size(self, file_name: str, file_format: str, x: int, y: int, width: int, height: int) -> str:
        """
        裁剪视频尺寸

        (x, y)：裁剪的起始坐标

        width：裁剪后的宽度， height：裁剪后的高度
        """
        self.__is_input_file()
        return os.popen(
            f'{self.__path} -i {self.__input_file} -vf "crop={width}:{height}:{x}:{y}" {file_name}.{file_format}').read()

    def trim_video_duration(self, file_name: str, file_format: str, start_time: str, end_time: str) -> str:
        """
        裁剪视频时长

        格式：时:分:秒.毫秒

        start_time：起始时间， end_time：结束时间
        """
        self.__is_input_file()
        return os.popen(
            f'{self.__path} -i {self.__input_file} -ss {start_time} -to {end_time} {file_name}.{file_format}').read()

    def rotate_video(self, file_name: str, file_format: str, angle: int) -> str:
        """旋转视频"""
        self.__is_input_file()
        return os.popen(
            f'{self.__path} -i {self.__input_file} -vf "transpose={angle}" {file_name}.{file_format}').read()

    def reverse_video(self, file_name: str, file_format: str) -> str:
        """反转视频"""
        self.__is_input_file()
        return os.popen(
            f'{self.__path} -i {self.__input_file} -vf "reverse" {file_name}.{file_format}').read()

    def mirror_video(self, file_name: str, file_format: str) -> str:
        """镜像视频"""
        self.__is_input_file()
        return os.popen(
            f'{self.__path} -i {self.__input_file} -vf "hflip" {file_name}.{file_format}').read()

    def modify_volume(self, file_name: str, file_format: str, volume: float) -> str:
        """修改音量"""
        self.__is_input_file()
        return os.popen(f'{self.__path} -i {self.__input_file} -af "volume={volume}" {file_name}.{file_format}').read()

    def screenshot(self, file_name: str, file_format: str, time: str) -> str:
        """截取视频帧"""
        self.__is_input_file()
        return os.popen(f'{self.__path} -i {self.__input_file} -ss {time} -vframes 1 {file_name}.{file_format}').read()

    def shell(self, command: str) -> str:
        """自定义处理文件"""
        return os.popen(f'{self.__path} -i {self.__input_file} {command}').read()


class Audio:
    def __init__(self, path: str = FFMPEG_PATH) -> None:
        self.__path = path
        self.__input_file = None

    def input_file(self, file: str) -> 'Audio':
        """输入文件"""
        self.__input_file = file
        return self

    def __is_input_file(self) -> None:
        """是否有输入文件"""
        if self.input_file is None:
            raise Exception('输入文件没有进行设置')

    def output_simple(self, file_name: str, file_format: str) -> str:
        """输出转换"""
        self.__is_input_file()
        return os.popen(f'{self.__path} -i {self.__input_file} {file_name}.{file_format}').read()

    def trim_audio_duration(self, file_name: str, file_format: str, start_time: str, end_time: str) -> str:
        """
        裁剪音频时长

        格式：时:分:秒.毫秒
        """
        self.__is_input_file()
        return os.popen(
            f'{self.__path} -i {self.__input_file} -ss {start_time} -to {end_time} {file_name}.{file_format}').read()

    def set_audio_multiplier(self, file_name: str, file_format: str, multiplier: float) -> str:
        """设置音频播放速度并输出 调整速度倍率范围[0.25, 4]"""
        self.__is_input_file()
        return os.popen(
            f'{self.__path} -i {self.__input_file} -af "atempo={multiplier}" {file_name}.{file_format}').read()

    def modify_volume(self, file_name: str, file_format: str, volume: float) -> str:
        """设置音频音量并输出 音量范围[0, 1]"""
        self.__is_input_file()
        return os.popen(f'{self.__path} -i {self.__input_file} -af "volume={volume}" {file_name}.{file_format}').read()

    def channel_processing(self, file_name: str, file_format: str, channel: int) -> str:
        """设置音频声道并输出 声道范围[1, 2]"""
        self.__is_input_file()
        return os.popen(f'{self.__path} -i {self.__input_file} -ac {channel} {file_name}.{file_format}').read()

    def set_audio_samplerate(self, file_name: str, file_format: str, samplerate: int) -> str:
        """设置音频采样率并输出 采样率范围[8000, 192000]"""
        self.__is_input_file()
        return os.popen(f'{self.__path} -i {self.__input_file} -ar {samplerate} {file_name}.{file_format}').read()

    def set_audio_bitrate(self, file_name: str, file_format: str, bitrate: int) -> str:
        """设置音频码率并输出 码率范围[32, 192000]"""
        self.__is_input_file()
        return os.popen(f'{self.__path} -i {self.__input_file} -b:a {bitrate}k {file_name}.{file_format}').read()

    def set_audio_quality(self, file_name: str, file_format: str, quality: int) -> str:
        """设置音频质量并输出 质量范围[0, 10]"""
        self.__is_input_file()
        return os.popen(f'{self.__path} -i {self.__input_file} -aq {quality} {file_name}.{file_format}').read()

    def shell(self, command: str) -> str:
        """自定义处理文件"""
        return os.popen(f'{self.__path} -i {self.__input_file} {command}').read()


class Subtitle:
    def __init__(self, path: str = FFMPEG_PATH) -> None:
        self.__path = path
        self.__input_file = None

    def input_file(self, file: str) -> 'Subtitle':
        """输入文件"""
        self.__input_file = file
        return self

    def __is_input_file(self) -> None:
        """是否有输入文件"""
        if self.input_file is None:
            raise Exception('输入文件没有进行设置')

    def output_simple(self, file_name: str, file_format: str) -> str:
        """输出转换"""
        self.__is_input_file()
        return os.popen(f'{self.__path} -i {self.__input_file} {file_name}.{file_format}').read()

    def trim_subtitle_duration(self, file_name: str, file_format: str, start_time: str, end_time: str) -> str:
        """
        裁剪字幕时长

        格式：时:分:秒.毫秒
        """
        self.__is_input_file()
        return os.popen(
            f'{self.__path} -i {self.__input_file} -ss {start_time} -to {end_time} {file_name}.{file_format}').read()

    def set_subtitle_multiplier(self, file_name: str, file_format: str, multiplier: float) -> str:
        """设置字幕播放速度并输出 调整速度倍率范围[0.25, 4]"""
        self.__is_input_file()
        return os.popen(
            f'{self.__path} -i {self.__input_file} -af "atempo={multiplier}" {file_name}.{file_format}').read()

    def set_subtitle_fontsize(self, file_name: str, file_format: str, fontsize: int) -> str:
        """设置字幕字体大小并输出 字体大小范围[8, 512]"""
        self.__is_input_file()
        return os.popen(
            f'{self.__path} -i {self.__input_file} -subfontsize {fontsize} {file_name}.{file_format}').read()

    def set_subtitle_color(self, file_name: str, file_format: str, color: str) -> str:
        """设置字幕颜色并输出 颜色范围[#000000, #FFFFFF]"""
        self.__is_input_file()
        return os.popen(f'{self.__path} -i {self.__input_file} -subcolor {color} {file_name}.{file_format}').read()

    def set_subtitle_font(self, file_name: str, file_format: str, font: str) -> str:
        """设置字幕字体并输出 字体范围[Arial, SimHei, SimSun, SimKai, SimFang, SimSun-PUA, SimKai-PUA, SimFang-PUA]"""
        self.__is_input_file()
        return os.popen(f'{self.__path} -i {self.__input_file} -subfont {font} {file_name}.{file_format}').read()

    def set_subtitle_position(self, file_name: str, file_format: str, position: str) -> str:
        """设置字幕位置并输出 位置范围[top, middle, bottom]"""
        self.__is_input_file()
        return os.popen(f'{self.__path} -i {self.__input_file} -subpos {position} {file_name}.{file_format}').read()

    def set_subtitle_alignment(self, file_name: str, file_format: str, alignment: str) -> str:
        """设置字幕对齐方式并输出 对齐方式范围[left, center, right]"""
        self.__is_input_file()
        return os.popen(f'{self.__path} -i {self.__input_file} -subalign {alignment} {file_name}.{file_format}').read()

    def set_subtitle_margin(self, file_name: str, file_format: str, margin: int) -> str:
        """设置字幕边距并输出 边距范围[0, 512]"""
        self.__is_input_file()
        return os.popen(f'{self.__path} -i {self.__input_file} -submargin {margin} {file_name}.{file_format}').read()

    def set_subtitle_delay(self, file_name: str, file_format: str, delay: int) -> str:
        """设置字幕延迟并输出 延迟范围[-3600, 3600]"""
        self.__is_input_file()
        return os.popen(f'{self.__path} -i {self.__input_file} -subdelay {delay} {file_name}.{file_format}').read()

    def shell(self, command: str) -> str:
        """自定义处理文件"""
        return os.popen(f'{self.__path} -i {self.__input_file} {command}').read()


class Synthesis:

    def __init__(self, path: str = FFMPEG_PATH) -> None:
        self.__path = path

    def audio_and_video_merger(self, audio_file: str, video_file: str, file_name: str, file_format: str) -> str:
        """音频和视频合并"""
        return os.popen(f'{self.__path} -i {audio_file} -i {video_file} -c copy {file_name}.{file_format}').read()

    def multiple_video_merger(self, video_files: list[str], file_name: str, file_format: str) -> str:
        """多视频合并"""
        with open('filelist.txt', 'w', encoding='utf-8') as f:
            for file in video_files:
                f.write(f"file '{file}'\n")
        return os.popen(f'{self.__path} -f concat -i filelist.txt -c copy {file_name}.{file_format}').read()

    def multiple_audio_merger(self, audio_files: list[str], file_name: str, file_format: str) -> str:
        """多音频合并"""
        with open('filelist.txt', 'w', encoding='utf-8') as f:
            for file in audio_files:
                f.write(f"file '{file}'\n")
        return os.popen(f'{self.__path} -f concat -i filelist.txt -c copy {file_name}.{file_format}').read()