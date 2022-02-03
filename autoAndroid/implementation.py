from math import ceil
import random
import time
from autoAndroid.api import *

# 点击指定坐标位置
def click(deviceID, x, y):
    print(f'当前动作 -> 点击：({ x }, { y })')
    touch(deviceID, x, y)

# 滑动操作
def slide(deviceID, x1, y1, x2, y2, second):
    print(f'当前动作 -> 滑动： 正在从 ({ x1 }, { y1 }) 到 ({ x2 }, { y2 }) 滑动， 滑动时间 { second }s')
    sliding(deviceID, x1, y1, x2, y2, second * 1000)

# 长按点击
def longClick(deviceID, x, y, second):
    print(f'当前动作 -> 长按点击：({ x }, { y })， 持续时间 { second }s')
    longTouch(deviceID, x, y, second * 1000)

# 监听图片出现 并且 返回图片所在区块的中心坐标
def watch(deviceID, imgPath, duration ,intervalTime, threshold):
    print(f'当前动作 -> 监听图片出现， 监听时间 { duration }s')
    rangeNumber = ceil(duration / intervalTime)
    for i in range(rangeNumber):
        print(f'开始匹配：第{ i + 1 }次， 一共{ rangeNumber }次')
        pos = comparison(deviceID, imgPath, threshold)
        if pos != None:
            print(f'匹配成功，找到目标 具体坐标：{ pos }')
            return pos
        if rangeNumber > 1: print(f'本次匹配：未匹配到目标, 等待下次匹配，等待时间 { intervalTime }s')
        time.sleep(intervalTime)
    print('监听期间未出现目标')

# 监听图片出现 并且 点击
def watchAndClick(deviceID, imgPath, duration ,intervalTime, threshold):
    pos = watch(deviceID, imgPath, duration ,intervalTime, threshold)
    if pos == None: return
    x, y = pos
    click(deviceID, x, y)

# 根据两张图片滑动操作
def imgAndSlide(deviceID, imgPath1, imgPath2, second, threshold):
    pos1 = watch(deviceID, imgPath1, 0.1, 0.1, threshold)
    if pos1 == None: return
    pos2 = watch(deviceID, imgPath2, 0.1, 0.1, threshold)
    if pos2 == None: return
    x1, y1 = pos1
    x2, y2 = pos2
    slide(deviceID, x1, y1, x2, y2, second)

# 监听图片出现 未出现 滑动 出现 返回图片所在区块的中心坐标
def watchNotSlide(deviceID, imgPath, x1, y1, x2, y2, second, maxnumber, threshold):
    for i in range(maxnumber):
        pos = watch(deviceID, imgPath, 0.1, 0.1, threshold)
        if pos != None: return pos
        slide(deviceID, x1, y1, x2, y2, second)
    print('滑动监听已达到上限，但未出现目标')

# 监听图片出现 未出现 滑动 出现 点击
def watchNotSlideAndClient(deviceID, imgPath, x1, y1, x2, y2, second, maxnumber, threshold):
    pos = watchNotSlide(deviceID, imgPath, x1, y1, x2, y2, second, maxnumber, threshold)
    if pos == None: return
    x, y = pos
    click(deviceID, x, y)

# 监听多张图片是否出现 出现一张就返回 或运算
def watchOrImgs(deviceID, imgPaths, duration ,intervalTime, threshold):
    for imgPath in imgPaths:
        pos = watch(deviceID, imgPath, duration ,intervalTime, threshold)
        if pos != None: return pos

# 等待
def sleep(second):
    print(f'当前动作 -> 等待， 等待时间 { second }s')
    time.sleep(second)

# 随机等待
def randomSleep(endSecond, startSecond):
    time.sleep(round(random.uniform(startSecond, endSecond), 1))

__all__ = ['click', 'watch', 'slide', 'longClick', 'watchAndClick', 'imgAndSlide', 'watchNotSlide', 'watchNotSlideAndClient', 'watchOrImgs', 'sleep', 'randomSleep']