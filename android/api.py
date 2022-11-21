import os
import cv2
import time

adbPath = r'android\adb\adb.exe'


def connectAdb(deviceID: str) -> str:
    """ 连接设备 """
    result = os.popen(f'{adbPath} connect {deviceID}')
    string = result.read()
    result.close()
    return string


def get_devices() -> str:
    """ 获取设备列表，每一个为deviceID """
    result = os.popen(f'{adbPath} devices')
    string = result.read()
    result.close()
    return string


def get_devices_list() -> list[dict[str, str]]:
    """ 获取设备列表，每一个为deviceID 按行数组返回 """
    result = os.popen(f'{adbPath} devices')
    string = result.readlines()
    result.close()
    arr = []
    for item in string[1:]:
        if item.strip() != '':
            temp = item.strip().split('\t')
            arr.append({
                'id': temp[0],
                'state': temp[1]
            })
    return arr


def kill_adb() -> str:
    """ 杀死ADB进程 """
    result = os.popen(f'{adbPath} kill-server')
    string = result.read()
    result.close()
    return string


def get_first_devices_id() -> str:
    """ 自动寻找第一个 device 设备的id """
    arr = get_devices_list()
    if len(arr) == 0:
        return None
    list_str = filter(lambda x: x['state'] == 'device', list_str)
    list_str = list(list_str)
    if len(list_str) == 0:
        return None
    deviceID = list_str[0]['id']
    return deviceID


def install_apk(deviceID: str, apkPath: str) -> None:
    """ 安装apk """
    command = f'{adbPath} -s {deviceID} install {apkPath}'
    os.system(command)


def uninstall_apk(deviceID: str, apkPath: str) -> None:
    """ 卸载apk """
    command = f'{adbPath} -s {deviceID} uninstall {apkPath}'
    os.system(command)


def get_package_name(deviceID: str, apkPath: str) -> str:
    """ 获取 apk 包名 """
    command = f'{adbPath} -s {deviceID} shell dumpsys package {apkPath}'
    result = os.popen(command)
    string = result.read()
    result.close()
    return string


def start_app(deviceID: str, apkPath: str) -> None:
    """ 启动app """
    command = f'{adbPath} -s {deviceID} shell am start -n {apkPath}'
    os.system(command)


def stop_app(deviceID: str, apkPath: str) -> None:
    """ 停止app """
    command = f'{adbPath} -s {deviceID} shell am force-stop {apkPath}'
    os.system(command)


def get_screen_size(deviceID: str) -> str:
    """ 获取屏幕分辨率 """
    command = f'{adbPath} -s {deviceID} shell wm size'
    result = os.popen(command)
    string = result.read()
    result.close()
    return string


def screen_capture(deviceID: str, capPath: str) -> bool:
    """ 设备屏幕截图，需给定did和本机截图保存路径 """
    # 截图指令
    command1 = f'{adbPath} -s {deviceID} shell screencap -p sdcard/adb_screenCap.png'
    # 保存到本地
    command2 = f'{adbPath} pull sdcard/adb_screenCap.png {capPath}'
    # # 删除截图
    command3 = f'{adbPath} -s {deviceID} shell rm sdcard/adb_screenCap.png'
    # 执行
    for row in [command1, command2, command3]:
        time.sleep(0.1)
        os.system(row)
    # 判断是否保存成功
    return os.path.exists(capPath)


def touch(deviceID: str, x: int, y: int) -> None:
    """ 模拟点击屏幕 """
    command = f'{adbPath} -s {deviceID} shell input touchscreen tap {x} {y}'
    os.system(command)


def sliding(deviceID: str, x1: int, y1: int, x2: int, y2: int, second: int) -> None:
    """ 模拟滑动屏幕 """
    command = f'{adbPath} -s {deviceID} shell input swipe {x1} {y1} {x2} {y2} {second}'
    os.system(command)


def long_touch(deviceID: str, x1: int, y1: int, second: int) -> None:
    """ 模拟长按屏幕 """
    sliding(deviceID, x1, y1, x1, y1, second)


def locate(source: str, imgPath: str, threshold: float) -> tuple[int, int]:
    """ 从 source 图片中查找 imgPath 图片所在的位置，当置信度大于 threshold 时返回找到的最大置信度位置的左上角坐标 """
    # 加载图片
    screen = cv2.imread(source)
    img = cv2.imread(imgPath)
    # 使用 TM_CCO-EFF_NORMED 算法寻找图片 最相似为 1 范围 0 ~ 1
    result = cv2.matchTemplate(screen, img, cv2.TM_CCOEFF_NORMED)
    # 获取 相似度 最高的 左上角位置 和 相似度
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= threshold:
        return max_loc
    else:
        return None


def center_of_touch_area(imgPath: str, pos: tuple[int, int]) -> tuple[int, int]:
    """ 给定目标位置和目标左上角顶点坐标，即可给出目标中心的坐标 """
    x, y = pos
    h, w, t = cv2.imread(imgPath).shape
    # 图片获取某一部出错 返回 None
    if x < 0 or y < 0 or h <= 0 or w <= 0:
        return None
    return x + w / 2, y + h / 2


def comparison(deviceID: str, imgPath: str, threshold: float) -> tuple[int, int]:
    """ 寻找图片中心坐标 """
    screen_capture(deviceID, 'screenCap.png')
    time.sleep(0.1)
    pos = locate('screenCap.png', imgPath, threshold)
    os.remove('screenCap.png')
    if pos is None:
        return None
    return center_of_touch_area(imgPath, pos)


__all__ = ['connectAdb', 'get_devices', 'get_devices_list', 'kill_adb', 'get_first_devices_id', 'screen_capture',
           'touch',
           'sliding', 'long_touch', 'comparison']
