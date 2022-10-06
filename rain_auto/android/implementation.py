from math import ceil
import random
import time
from rain_auto.android.api import *


def click(deviceID, x, y):
    """ 点击指定坐标位置 """
    print(f'当前动作 -> 点击：({x}, {y})')
    touch(deviceID, x, y)


def slide(deviceID, x1, y1, x2, y2, second):
    """ 滑动操作 """
    print(f'当前动作 -> 滑动： 正在从 ({x1}, {y1}) 到 ({x2}, {y2}) 滑动， 滑动时间 {second}s')
    sliding(deviceID, x1, y1, x2, y2, second * 1000)


def long_click(deviceID, x, y, second):
    """ 长按点击 """
    print(f'当前动作 -> 长按点击：({x}, {y})， 持续时间 {second}s')
    long_touch(deviceID, x, y, second * 1000)


def watch(deviceID, imgPath, duration, intervalTime, threshold):
    """ 监听图片出现 并且 返回图片所在区块的中心坐标 """
    img = imgPath.split('/')[-1]
    print(f'当前动作 -> 监听图片出现， 监听时间 {duration}s， 监听图片 {img}')
    rangeNumber = ceil(duration / intervalTime)
    for i in range(rangeNumber):
        print(f'开始匹配：第{i + 1}次， 一共{rangeNumber}次')
        pos = comparison(deviceID, imgPath, threshold)
        if pos is not None:
            print(f'匹配成功，找到目标 具体坐标：{pos}')
            return pos
        if rangeNumber > 1:
            print(f'本次匹配：未匹配到目标, 等待下次匹配，等待时间 {intervalTime}s')
        time.sleep(intervalTime)
    print('监听期间未出现目标')


def watch_and_click(deviceID, imgPath, duration, intervalTime, threshold):
    """ 监听图片出现 并且 点击 """
    pos = watch(deviceID, imgPath, duration, intervalTime, threshold)
    if pos is None:
        return None
    x, y = pos
    click(deviceID, x, y)


def img_and_slide(deviceID, imgPath1, imgPath2, second, threshold):
    """ 根据两张图片滑动操作 """
    pos1 = watch(deviceID, imgPath1, 0.1, 0.1, threshold)
    if pos1 is None:
        return None
    pos2 = watch(deviceID, imgPath2, 0.1, 0.1, threshold)
    if pos2 is None:
        return None
    x1, y1 = pos1
    x2, y2 = pos2
    slide(deviceID, x1, y1, x2, y2, second)


def watch_not_slide(deviceID, imgPath, x1, y1, x2, y2, second, maxnumber, threshold):
    """ 监听图片出现 未出现 滑动 出现 返回图片所在区块的中心坐标 """
    for i in range(maxnumber):
        pos = watch(deviceID, imgPath, 0.1, 0.1, threshold)
        if pos is not None:
            return pos
        slide(deviceID, x1, y1, x2, y2, second)
    print('滑动监听已达到上限，但未出现目标')


def watch_not_slide_and_client(deviceID, imgPath, x1, y1, x2, y2, second, maxnumber, threshold):
    """ 监听图片出现 未出现 滑动 出现 点击 """
    pos = watch_not_slide(deviceID, imgPath, x1, y1, x2, y2, second, maxnumber, threshold)
    if pos is None:
        return None
    x, y = pos
    click(deviceID, x, y)


def watch_or_images(deviceID, imgPaths, duration, intervalTime, threshold):
    """ 监听多张图片是否出现 出现一张就返回 或运算 """
    for imgPath in imgPaths:
        pos = watch(deviceID, imgPath, duration, intervalTime, threshold)
        if pos is not None:
            return pos


def sleep(second):
    """ 等待 """
    print(f'当前动作 -> 等待， 等待时间 {second}s')
    time.sleep(second)


def random_sleep(end_second, start_second):
    """ 随机等待 """
    time.sleep(round(random.uniform(end_second, start_second), 1))


__all__ = ['click', 'watch', 'slide', 'long_click', 'watch_and_click', 'img_and_slide', 'watch_not_slide',
           'watch_not_slide_and_client', 'watch_or_images', 'sleep', 'random_sleep']
