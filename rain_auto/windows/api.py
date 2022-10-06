import time
from math import ceil

import pyautogui
import pyperclip
from rain_auto.windows.capture import target_identification, target_identification_all
from rain_auto.windows.windows import get_hWnd, set_window_foreground, set_window_pos

# 保护措施
pyautogui.FAILSAFE = True


def mouse_move(x: int, y: int, duration: float = 0.1):
    """ 鼠标移动 """
    print(f'当前动作 -> 鼠标移动({x}, {y})， 持续时间 {duration}s')
    pyautogui.moveTo(x, y, duration)


def left_click(x: int, y: int):
    """ 左键单击 """
    print(f'当前动作 -> 左键单击({x}, {y})')
    pyautogui.leftClick(x, y)


def right_click(x: int, y: int):
    """ 右键单击 """
    print(f'当前动作 -> 右键单击({x}, {y})')
    pyautogui.rightClick(x, y)


def middle_click(x: int, y: int):
    """ 中键单击 """
    print(f'当前动作 -> 中键单击({x}, {y})')
    pyautogui.middleClick(x, y)


def double_click(x: int, y: int):
    """ 左键双击 """
    print(f'当前动作 -> 左键双击({x}, {y})')
    pyautogui.doubleClick(x, y)


def drag_to(x: int, y: int):
    """ 左键拖动 """
    print(f'当前动作 -> 左键拖动，拖动到({x}, {y})')
    pyautogui.dragTo(x, y, button='left')


def scroll(clicks: int):
    """ 滚动 按格 这个方法 正值向下 (pyautogui 默认 负值向下 ) """
    print(f'当前动作 -> 滚动，滚动到{clicks}格')
    pyautogui.scroll(-clicks)


def write(text: str | list[str]):
    """ 输入内容 """
    print(f'当前动作 -> 输入内容，内容为：{text}')
    pyautogui.typewrite(text)


def key_down(key: str):
    """ 按下按键 """
    print(f'当前动作 -> 按下按键，按键为：{key}')
    pyautogui.keyDown(key)


def key_up(key: str):
    """ 松开按键 """
    print(f'当前动作 -> 松开按键，按键为：{key}')
    pyautogui.keyUp(key)


def key_down_up(key: str):
    """ 点击按键， 是 key_down 加 key_up 组合 """
    print(f'当前动作 -> 点击按键，按键为：{key}')
    pyautogui.press(key)


def hotkey(*keys: tuple[str]):
    """ 输入组合键 """
    print(f'当前动作 -> 触发组合键, 组合键是：{" + ".join(keys)}')
    pyautogui.hotkey(*keys)


def copy(text: str):
    """ 复制到剪贴板 """
    print(f'当前动作 -> 复制到剪贴板， 复制语句 {text}')
    pyperclip.copy(text)


def paste():
    """ 粘贴剪贴板语句 """
    string = pyperclip.paste()
    print(f'当前动作 -> 粘贴剪贴板语句, 粘贴语句 {string}')
    hotkey('Ctrl', 'v')


def watch(img_path: str, window_title: str, duration: int = 60, intervalTime: int = 1):
    """ 监听图片出现 并且 返回图片所在区块的中心坐标 """
    print(f'当前动作 -> 监听图片出现， 监听时间 {duration}s')
    rangeNumber = ceil(duration / intervalTime)
    for i in range(rangeNumber):
        print(f'开始匹配：第{i + 1}次， 一共{rangeNumber}次')
        pos = target_identification(img_path, window_title)
        if pos is not None:
            print(f'匹配成功，找到目标 具体坐标：{pos}')
            return pos
        if rangeNumber > 1:
            print(f'本次匹配：未匹配到目标, 等待下次匹配，等待时间 {intervalTime}s')
        time.sleep(intervalTime)
    print('监听期间未出现目标')


def watch_all(img_path: str, window_title: str, duration: int = 60, intervalTime: int = 1, accuracy: float = 0.5):
    """ 监听图片出现 并且 返回满足条件图片全部中心坐标（自动去重） """
    print(f'当前动作 -> 监听图片出现， 监听时间 {duration}s')
    rangeNumber = ceil(duration / intervalTime)
    for i in range(rangeNumber):
        print(f'开始匹配：第{i + 1}次， 一共{rangeNumber}次')
        pos = target_identification_all(img_path, window_title, accuracy)
        if pos is not None:
            print(f'匹配成功，找到目标组 具体坐标：{pos}')
            return pos
        if rangeNumber > 1: print(f'本次匹配：未匹配到目标, 等待下次匹配，等待时间 {intervalTime}s')
        time.sleep(intervalTime)
    print('监听期间未出现目标')


def window_foreground(window_title: str) -> int:
    """ 窗口置顶 """
    hWnd = get_hWnd(window_title)
    set_window_foreground(hWnd)
    set_window_pos(hWnd)
    time.sleep(0.005)
    return hWnd


__all__ = ['mouse_move', 'left_click', 'right_click', 'middle_click', 'double_click', 'drag_to', 'scroll', 'write',
           'window_foreground', 'key_down', 'key_up', 'key_down_up', 'hotkey', 'copy', 'paste', 'watch', 'watch_all']
