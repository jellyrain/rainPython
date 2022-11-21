import time
from windows.window_api import get_hWnd_fuzzy, set_window_foreground, set_window_pos
from windows.cores import watch, left_click


def window_foreground_fuzzy(window_title: str) -> int:
    """ 传入窗口名字，将窗口置顶且返回窗口句柄 """
    hWnd = get_hWnd_fuzzy(window_title)
    set_window_foreground(hWnd)
    set_window_pos(hWnd)
    time.sleep(0.005)
    return hWnd


def watch_and_left_click(hWnd: int, img_path: str, duration: int = 60, intervalTime: int = 1) -> None:
    """ 监听图片出现 并且 点击 """
    pos = watch(hWnd, img_path, duration, intervalTime)
    if pos is None:
        return None
    left_click(hWnd, pos)
