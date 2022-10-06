import os
import time


class File:

    def __init__(self, path: str) -> None:
        self.__path = os.path.abspath(path)
        self.__name = os.path.basename(path)

    def get_path(self):
        """获取文件绝对路径"""
        return self.__path

    def get_name(self):
        """获取文件名"""
        return self.__name

    def get_size(self):
        """获取文件大小"""
        return os.path.getsize(self.__path)

    def get_extension(self):
        """获取文件扩展名"""
        return os.path.splitext(self.__path)[1]

    def get_content(self):
        """获取文件内容"""
        with open(self.__path, 'r') as f:
            return f.read()

    def get_lines(self):
        """获取文件行数"""
        with open(self.__path, 'r') as f:
            return len(f.readlines())

    def get_words(self):
        """获取文件单词数"""
        with open(self.__path, 'r') as f:
            return len(f.read().split())

    def get_chars(self):
        """获取文件字符数"""
        with open(self.__path, 'r') as f:
            return len(f.read())

    def get_file_create_time(self):
        """获取文件创建时间"""
        return os.path.getctime(self.__path)

    def get_file_access_time(self):
        """获取文件最后访问时间"""
        return os.path.getatime(self.__path)

    def get_file_change_time(self):
        """获取文件最后修改时间"""
        return os.path.getmtime(self.__path)

    def get_file_create_time_format(self):
        """获取文件创建时间格式化"""
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getctime(self.__path)))

    def get_file_access_time_format(self):
        """获取文件最后访问时间格式化"""
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getatime(self.__path)))

    def get_file_change_time_format(self):
        """获取文件最后修改时间格式化"""
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(self.__path)))

    def set_file_change_time(self, change_time):
        """设置文件最后修改时间"""
        os.utime(self.__path, (os.path.getatime(self.__path), change_time))

    def set_file_access_time(self, access_time):
        """设置文件最后访问时间"""
        os.utime(self.__path, (access_time, os.path.getmtime(self.__path)))

    def get_file_status(self):
        """获取文件状态"""
        return os.stat(self.__path)


__all = ['File']