from math import ceil
import random
import time
from android.api import *


def click(deviceID: str, pos: tuple[int, int]) -> None:
    """ 点击指定坐标位置 """
    x, y = pos
    print(f'当前动作 -> 点击：({x}, {y})')
    touch(deviceID, x, y)


def slide(deviceID: str, pos1: tuple[int, int], pos2: tuple[int, int], second: int) -> None:
    x1, y1 = pos1
    x2, y2 = pos2
    """ 滑动操作 """
    print(f'当前动作 -> 滑动： 正在从 ({x1}, {y1}) 到 ({x2}, {y2}) 滑动， 滑动时间 {second}s')
    sliding(deviceID, x1, y1, x2, y2, second * 1000)


def long_click(deviceID: str, pos: tuple[int, int], second: int) -> None:
    """ 长按点击 """
    x, y = pos
    print(f'当前动作 -> 长按点击：({x}, {y})， 持续时间 {second}s')
    long_touch(deviceID, x, y, second * 1000)


def watch(deviceID: str, imgPath: str, duration: int = 60, intervalTime: int = 1, threshold: float = 0.7) -> tuple[
                                                                                                                 int, int] | None:
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


def sleep(second):
    """ 等待 """
    print(f'当前动作 -> 等待， 等待时间 {second}s')
    time.sleep(second)


def random_sleep(end_second, start_second):
    """ 随机等待 """
    time.sleep(round(random.uniform(end_second, start_second), 1))


__all__ = ['click', 'watch', 'slide', 'long_click', 'sleep', 'random_sleep']
