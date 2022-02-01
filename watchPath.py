import os
import re

def relativePath(path, relative):
    if re.findall('^../', relative): 
        path = path.split('\\')[0 : -1]
        path = '\\'.join(path)
        if(path[-1] == ':'): path = path + '\\'
        relative = relative.split('/')[1:]
        relative = '/'.join(relative)
        path, relative = relativePath(path,relative)

    if re.findall('^./', relative):
        relative = relative.split('/')[1:]
        relative = '/'.join(relative)
        path, relative = relativePath(path,relative) 

    return path, relative

def relativeMethod(path, relative):
    path, relative = relativePath(path,relative) 
    if relative:
        return os.path.join(path, relative)
    else:
        return path

# 监听单层目录
class WatchPath:
    def __init__(self, dirName=None, refresh = True):
        self.path = os.getcwd()
        if dirName != None: self.path = os.path.join(self.path, dirName)
        if refresh: self.refresh()

    @staticmethod 
    def createAbsolute(path):
        p = WatchPath(refresh = False)
        p.path = '\\'.join(path.split('/')) if re.findall('/', path) else path
        p.refresh()
        return p

    def absolute(self, path):
        self.path = path
        self.refresh()

    def relative(self, relative):
        self.path = relativeMethod(self.path, relative)
        self.refresh()

    def refresh(self):
        self.files = {}
        self.dirs = {}
        for fd in os.scandir(self.path):
            if fd.is_dir(): self.dirs[fd.name] = fd
            if fd.is_file(): self.files[fd.name] = fd

    def oneDir(self, dirName):
        return self.dirs[dirName]

    def oneFile(self, fileName):
        return self.files[fileName]

    def fileSuffix(self, suffix):
        result = {}
        for file in self.files:
            if re.findall(f'.{suffix}$', file): result[file] = self.files[file]
        return result

    def fileNameInclude(self, includeStr):
        result = {}
        for file in self.files:
            if re.findall(f'{includeStr}', file): result[file] = self.files[file]
        return result

    def dirNameInclude(self, includeStr):
        result = {}
        for dirs in self.dirs:
            if re.findall(f'{includeStr}', dirs): result[dirs] = self.dirs[dirs]
        return result

    def fileHash(self, file):
        h = hash(file)
        result = {}
        for file in self.files:
            if hash(file) == h: result[file] = self.files[file]
        return result

# 深层监听目录
class DeepWatchPath:
    def __init__(self, dirName=None):
        self.path = WatchPath(dirName)
        self.children =[]
        if len(self.path.dirs) > 0: self.__deep(dirName)

    def __deep(self, dirName):
        self.children = []
        for dirs in self.path.dirs:
            self.children.append(DeepWatchPath(os.path.join(dirName, dirs) if dirName is not None else dirs))

    def lookup(self):
        self.path.lookup()
        for child in self.children:
            child.lookup()

    def fileNameInclude(self, includeStr):
        temp = self.path.fileNameInclude(includeStr)
        result = { self.path.path : temp } if temp != {} else {}
        for child in self.children:
            result.update(child.fileNameInclude(includeStr))
        return result

    def dirNameInclude(self, includeStr):
        temp = self.path.dirNameInclude(includeStr) 
        result = { self.path.path : temp } if temp != {} else {}
        for child in self.children:
            result.update(child.dirNameInclude(includeStr))
        return result

    def fileHash(self, file):
        temp = self.path.fileHash(file) 
        result = { self.path.path : temp } if temp != {} else {}
        for child in self.children:
            result.update(child.fileHash(file))
        return result

# 获取文件路径 会深层遍历 条件 文件的全名必须只有一个 否则 只会返回第一个符合名字的路径 需要多个路径 请使用  DeepWatchPath 类方法获取
def getPath(fileName):
    temp = DeepWatchPath().fileNameInclude(fileName)
    return os.path.join(list(temp.keys())[0], fileName)

__all__ = ['WatchPath', 'DeepWatchPath', 'getPath']