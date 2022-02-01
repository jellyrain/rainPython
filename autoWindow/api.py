import os, time
import pyautogui
import cv2, numpy

# 屏幕截图，本机截图保存路径
def screenCapture(capPath):
    # 截图
    pyautogui.screenshot().save(capPath)
    # 判断是否保存成功
    if os.path.exists(capPath) == True:
        return True
    else:
        return False

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

# 从source图片中查找wanted图片所在的位置，当置信度大于accuracy时返回找到的所有位置的左上角坐标（自动去重）
def locateAll(source, imgPath, accuracy):
    loc_pos = []
    screen = cv2.imread(source)
    img = cv2.imread(imgPath)
    # 使用 TM_CCOEFF_NORMED 算法寻找图片 最相似为 1 范围 0 ~ 1
    result = cv2.matchTemplate(screen, img, cv2.TM_CCOEFF_NORMED)
    # 筛选对比度大于预期的全部值
    location = numpy.where(result >= accuracy)
    ex, ey = 0, 0
    for pt in zip(*location[::-1]):
        x = pt[0]
        y = pt[1]
        if (x - ex) + (y - ey) < 15:  # 去掉邻近重复的点
            continue
        ex, ey = x, y
        loc_pos.append((int(x), int(y)))
    return loc_pos

# 给定目标位置和目标左上角顶点坐标，即可给出目标中心的坐标
def centerOfTouchArea(imgPath, pos):
    x, y = pos
    h, w, t  = cv2.imread(imgPath).shape
    # 图片获取某一部出错 返回 None
    if x < 0 or y < 0 or h <= 0 or w <= 0 : return None
    return (x + w / 2, y + h / 2)

# 寻找图片中心坐标
def comparison(imgPath, threshold):
    screenCapture('screenCap.png')
    time.sleep(0.1)
    pos = locate('screenCap.png', imgPath, threshold)
    os.remove('screenCap.png')
    if pos == None: return None
    return centerOfTouchArea(imgPath, pos)

# 寻找满足条件图片全部中心坐标（自动去重）
def comparisonAll(imgPath, threshold):
    screenCapture('screenCap.png')
    time.sleep(0.1)
    poss = locateAll('screenCap.png', imgPath, threshold)
    os.remove('screenCap.png')
    if len(poss) == 0: return None
    result = []
    for pos in poss:
        temp = centerOfTouchArea(imgPath, pos)
        if temp != None: result.append(temp)
    return result

__all__ = ['comparison', 'comparisonAll']