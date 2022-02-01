import os
import cv2
import time

adbPath = r'autoAndroid\adb\adb.exe'

# 连接设备
def connectAdb(deviceID):
    return os.popen(f'{ adbPath } connect { deviceID }').read()

# 获取设备列表，每一个为deviceID
def getDevices():
    return os.popen(f'{ adbPath } devices').read()

# 杀死ADB进程
def killAdb():
    return os.popen(f'{ adbPath } kill-server')

# 设备屏幕截图，需给定did和本机截图保存路径
def screenCapture(deviceID, capPath):
    # 截图指令
    command1 = f'{ adbPath } -s { deviceID } shell screencap -p sdcard/adb_screenCap.png'
    # 保存到本地
    command2 = f'{ adbPath } pull sdcard/adb_screenCap.png { capPath }'
    # # 删除截图
    command3 = f'{ adbPath } -s { deviceID } shell rm sdcard/adb_screenCap.png'
    # 执行
    for row in [command1, command2]:
        time.sleep(0.1)
        os.system(row)
    # 判断是否保存成功
    if os.path.exists(capPath) == True:
        return True
    else:
        return False

# 模拟点击屏幕
def touch(deviceID, x, y):
    command = f'{ adbPath } -s { deviceID } shell input touchscreen tap { x } { y }'
    os.system(command)

# 模拟滑动屏幕
def sliding(deviceID, x1, y1, x2, y2, second):
    command = f'{ adbPath } -s { deviceID } shell input swipe { x1 } { y1 } { x2 } { y2 } { second }'
    os.system(command)

# 模拟长按屏幕
def longTouch(deviceID, x1, y1, second):
    sliding(deviceID, x1, y1, x1, y1, second)

# 从 source 图片中查找 imgPath 图片所在的位置，当置信度大于 threshold 时返回找到的最大置信度位置的左上角坐标
def locate(source, imgPath, threshold):
    # 加载图片
    screen = cv2.imread(source)
    img = cv2.imread(imgPath)
    # 使用 TM_CCOEFF_NORMED 算法寻找图片 最相似为 1 范围 0 ~ 1
    result = cv2.matchTemplate(screen, img, cv2.TM_CCOEFF_NORMED)
    # 获取 相似度 最高的 左上角位置 和 相似度
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= threshold:
        return max_loc
    else:
        return None

# 给定目标位置和目标左上角顶点坐标，即可给出目标中心的坐标
def centerOfTouchArea(imgPath, pos):
    x, y = pos
    h, w, t  = cv2.imread(imgPath).shape
    # 图片获取某一部出错 返回 None
    if x < 0 or y < 0 or h <= 0 or w <= 0 : return None
    return (x + w / 2, y + h / 2)

# 寻找图片中心坐标
def comparison (deviceID, imgPath, threshold):
    screenCapture(deviceID, 'screenCap.png')
    time.sleep(0.1)
    pos = locate('screenCap.png', imgPath, threshold)
    os.remove('screenCap.png')
    if pos == None: return None
    return centerOfTouchArea(imgPath, pos)

__all__ = ['connectAdb', 'getDevices', 'killAdb', 'screenCapture', 'touch', 'sliding', 'longTouch', 'comparison']