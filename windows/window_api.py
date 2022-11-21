import re
from ctypes import windll
from win32gui import FindWindow, FindWindowEx, EnumWindows, GetWindowText, GetWindowRect, SetForegroundWindow


def hWnd_dict(hWnd: int) -> dict[str, str | int]:
    """ 句柄封装为带标题的对象 """
    return {
        'title': GetWindowText(hWnd),
        'hWnd': hWnd
    }


def get_hWnd(window_title: str) -> int:
    """ 获取第一个满足标题的句柄 """
    return FindWindow(None, window_title)


def get_window_hWnd(window_title: str) -> None | dict[str, str | int] | list[dict[str, str | int]]:
    """ 获取全部同名的窗扣口句柄 如果只有一个返回一个字典，如果有多个返回列表字典 """
    hWnd_list = []
    # 获取第一个句柄
    hWnd = FindWindow(None, window_title)
    if hWnd == 0:
        return None
    hWnd_list.append(hWnd_dict(hWnd))
    # 遍历获取其他句柄
    while 1:
        hWnd = FindWindowEx(None, hWnd, None, window_title)
        if hWnd == 0:
            break
        hWnd_list.append(hWnd_dict(hWnd))
    return hWnd_list if len(hWnd_list) > 1 else hWnd_list[0]


def get_all_window_hWnd() -> list[dict[str, str | int]]:
    """ 获取所有带名字的窗口句柄 """
    hWnd_list = []
    EnumWindows(lambda hWnd, param: param.append(hWnd), hWnd_list)
    return [hWnd_dict(item) for item in hWnd_list if GetWindowText(item) != '']


def get_hWnd_fuzzy(window_title: str) -> int:
    """ 正则模糊匹配第一个满足标题的句柄 """
    for item in get_all_window_hWnd():
        if re.search(window_title, item['title']):
            return item['hWnd']
    return 0


def get_window_rect(hWnd: int) -> dict[str, int]:
    """ 获取窗口坐标 """
    left, top, right, bottom = GetWindowRect(hWnd)
    return {
        'left': left,
        'top': top,
        'right': right,
        'bottom': bottom,
        'width': right - left,
        'height': bottom - top
    }


def set_window_foreground(hWnd: int) -> None:
    """ 设置窗口到最前面 """
    SetForegroundWindow(hWnd)


def set_window_pos(hWnd: int, x: int = 0, y: int = 0) -> None:
    """ 把窗口左上角移动到指定位置 """
    windll.user32.SetWindowPos(hWnd, 0, x, y, 0, 0, 0x0001 | 0x0004)


__all__ = ['get_hWnd', 'get_all_window_hWnd', 'get_hWnd_fuzzy', 'get_window_rect', 'set_window_foreground', 'set_window_pos']
