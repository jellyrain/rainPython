from android.cores import watch, slide, click


def watch_and_click(deviceID: str, imgPath: str, duration: int = 60, intervalTime: int = 1,
                    threshold: float = 0.7) -> None:
    """ 监听图片出现 并且 点击 """
    pos = watch(deviceID, imgPath, duration, intervalTime, threshold)
    if pos is None:
        return None
    click(deviceID, pos)


def img_and_slide(deviceID: str, imgPath1: str, imgPath2: str, second: int = 1, threshold: float = 0.7) -> None:
    """ 根据两张图片滑动操作 """
    pos1 = watch(deviceID, imgPath1, 0.1, 0.1, threshold)
    if pos1 is None:
        return None
    pos2 = watch(deviceID, imgPath2, 0.1, 0.1, threshold)
    if pos2 is None:
        return None
    slide(deviceID, pos1, pos2, second)


def watch_not_slide(deviceID: str, imgPath: str, pos1: tuple[int, int], pos2: tuple[int, int], second: int = 1,
                    max_number: int = 5, threshold: float = 0.7) -> tuple[int, int] | None:
    """ 监听图片出现 未出现 滑动 出现 返回图片所在区块的中心坐标 """
    for i in range(max_number):
        pos = watch(deviceID, imgPath, 0.1, 0.1, threshold)
        if pos is not None:
            return pos
        slide(deviceID, pos1, pos2, second)
    print('滑动监听已达到上限，但未出现目标')


def watch_not_slide_and_client(deviceID: str, imgPath: str, pos1: tuple[int, int], pos2: tuple[int, int],
                               second: int = 1, max_number: int = 5, threshold: float = 0.7):
    """ 监听图片出现 未出现 滑动 出现 点击 """
    pos = watch_not_slide(deviceID, imgPath, pos1, pos2, second, max_number, threshold)
    if pos is None:
        return None
    x, y = pos
    click(deviceID, x, y)
