import os, json

from vacc.FFprobe.config import FFPROBE_PATH

class FFprobe:
    def __init__(self, path: str = FFPROBE_PATH):
        self.__path = path
        self.__json = None

    def input_file(self, file: str) -> 'FFprobe':
        """输入文件"""
        self.__json = os.popen(f'{self.__path} -show_format -show_streams -of json {file}').read()
        return self

    def __is_input_file(self) -> None:
        """是否有输入文件"""
        if self.__json is None:
            raise Exception('输入文件没有进行设置')

    def get_json(self) -> str:
        """获取视频分析后的 json 数据"""
        self.__is_input_file()
        return self.__json

    def get_streams(self) -> list[dict]:
        """获取视频所有流数据"""
        self.__is_input_file()
        return json.loads(self.__json)['streams']

    def get_format(self) -> dict:
        """获取视频格式数据"""
        self.__is_input_file()
        return json.loads(self.__json)['format']

    def get_stream(self, stream_id: int) -> dict:
        """获取指定id视频流数据"""
        self.__is_input_file()
        return [stream for stream in self.get_streams() if stream['index'] == stream_id][0]

    def get_stream_type(self, stream_id: int) -> str:
        """获取指定id视频流类型"""
        self.__is_input_file()
        return self.get_stream(stream_id)['codec_type']

    def get_stream_codec(self, stream_id: int) -> str:
        """获取指定id视频流编码"""
        self.__is_input_file()
        return self.get_stream(stream_id)['codec_name']

    def get_stream_codec_long(self, stream_id: int) -> str:
        """获取指定id视频流编码名称"""
        self.__is_input_file()
        return self.get_stream(stream_id)['codec_long_name']

    def get_stream_codec_tag_version(self, stream_id: int) -> str:
        """获取指定id视频流编码标签版本"""
        self.__is_input_file()
        return self.get_stream(stream_id)['codec_tag_string']

    def get_stream_bit_rate(self, stream_id: int) -> str:
        """获取指定id视频流码率"""
        self.__is_input_file()
        return self.get_stream(stream_id)['bit_rate']