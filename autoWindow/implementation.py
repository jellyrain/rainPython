from math import ceil
import time
import pyautogui, pyperclip
from autoWindow.api import *

# 保护措施
pyautogui.FAILSAFE = True

# 鼠标移动
def mouseMove(x, y, duration):
    print(f'当前动作 -> 鼠标移动({ x }, { y })， 持续时间 { duration }s')
    pyautogui.moveTo(x, y, duration)

# 左键单击
def leftClick(x, y):
    print(f'当前动作 -> 左键单击({ x }, { y })')
    pyautogui.leftClick(x, y)

# 右键单击
def rightClick(x, y):
    print(f'当前动作 -> 右键单击({ x }, { y })')
    pyautogui.rightClick(x, y)

# 中键单击
def middleClick(x, y):
    print(f'当前动作 -> 中键单击({ x }, { y })')
    pyautogui.middleClick(x, y)

# 左键双击
def doubleClick(x, y):
    print(f'当前动作 -> 左键双击({ x }, { y })')
    pyautogui.doubleClick(x, y)

# 左键拖动
def dragTo(x, y):
    print(f'当前动作 -> 左键拖动，拖动到({ x }, { y })')
    pyautogui.dragTo(x, y, button = 'left')

# 滚动 按格 这个方法 正值向下 (pyautogui 默认 负值向下 )
def scroll(clicks):
    print(f'当前动作 -> 滚动，滚动到{ clicks }格')
    pyautogui.scroll(-clicks)

# 监听图片出现 并且 返回图片所在区块的中心坐标
def watch(imgPath, duration = 60 ,intervalTime = 1, threshold = 0.7):
    print(f'当前动作 -> 监听图片出现， 监听时间 { duration }s')
    rangeNumber = ceil(duration / intervalTime)
    for i in range(rangeNumber):
        print(f'开始匹配：第{ i + 1 }次， 一共{ rangeNumber }次')
        pos = comparison(imgPath, threshold)
        if pos != None:
            print(f'匹配成功，找到目标 具体坐标：{ pos }')
            return pos
        if rangeNumber > 1: print(f'本次匹配：未匹配到目标, 等待下次匹配，等待时间 { intervalTime }s')
        time.sleep(intervalTime)
    print('监听期间未出现目标')

# 监听图片出现 并且 返回满足条件图片全部中心坐标（自动去重）
def watchALL(imgPath, duration = 60 ,intervalTime = 1, threshold = 0.7):
    print(f'当前动作 -> 监听图片出现， 监听时间 { duration }s')
    rangeNumber = ceil(duration / intervalTime)
    for i in range(rangeNumber):
        print(f'开始匹配：第{ i + 1 }次， 一共{ rangeNumber }次')
        pos = comparisonAll(imgPath, threshold)
        if pos != None:
            print(f'匹配成功，找到目标组 具体坐标：{ pos }')
            return pos
        if rangeNumber > 1: print(f'本次匹配：未匹配到目标, 等待下次匹配，等待时间 { intervalTime }s')
        time.sleep(intervalTime)
    print('监听期间未出现目标')

# 复制到剪贴板
def copy(string):
    print(f'当前动作 -> 复制到剪贴板， 复制语句 { string }')
    pyperclip.copy(string)

# 粘贴剪贴板语句
def paste():
    string = pyperclip.paste()
    print(f'当前动作 -> 粘贴剪贴板语句, 粘贴语句 { string }')

__all__ = ['mouseMove', 'leftClick', 'rightClick', 'middleClick', 'doubleClick', 'dragTo', 'scroll', 'watch', 'watchAll', 'copy', 'paste']