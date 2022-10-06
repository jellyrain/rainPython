from time import sleep, time
from PIL import ImageGrab
import cv2
from numpy import asarray, where, ndarray
from rain_auto.windows import window_foreground, get_window_rect


def screen(hWnd: int) -> ndarray:
    """ 截图 """
    left, top, right, bottom, width, height = get_window_rect(hWnd).values()
    img = ImageGrab.grab((left, top, right, bottom))
    b, g, r = cv2.split(asarray(img))
    return cv2.merge([r, g, b])


def capture(window_title: str) -> ndarray:
    """ 截图 转换成 cv2 可以识别的 ndarray """
    hWnd = window_foreground(window_title)
    return screen(hWnd)


def continuous_screen(window_title: str, pictures: int, img_path: str, screen_sleep_seconds: float = 0.1,
                      sleep_seconds: int = 10) -> None:
    """ 批量截图 """
    hWnd = window_foreground(window_title)
    print(f'等待{sleep_seconds}秒')
    sleep(sleep_seconds)
    print('开始截图........')
    t1 = time()
    for i in range(pictures):
        img = screen(hWnd)
        cv2.imwrite(f'{img_path}/{str(i)}.png', img)
        sleep(screen_sleep_seconds)
    t2 = time()
    print(f'截图平均时间间隔为：{(t2 - t1) / pictures}')


def video_screen(video_path: str, img_path: str, interval: int = 10) -> None:
    # 读取视频
    cap = cv2.VideoCapture(video_path)
    # 获取视频总帧数
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    # 起始截取帧位置
    start_frame = 1

    flag = 0
    while cap.isOpened():
        cap.set(cv2.CAP_PROP_POS_MSEC, flag)
        cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

        ret, img = cap.read()
        cv2.waitKey(2000)
        cv2.imwrite((img_path + "/{}.png").format(flag), img)
        flag += 1
        start_frame += interval
        if start_frame >= frame_count:
            break


def template_matching(img_path: str, window_title: str) -> tuple:
    """ 对比两张图 截图（灰度图），原图（保留Alpha通道），返回比较结果 """
    img = capture(window_title)
    # 转为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    # 读取图片，并保留Alpha通道
    template_img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    # 取出Alpha通道
    alpha = template_img[:, :, 2]
    template_img = cv2.cvtColor(template_img, cv2.COLOR_BGRA2GRAY)
    # 模板匹配，将 alpha 作为 mask，TM_CORR_NORMED 方法的计算结果范围为[0, 1]，越接近1越匹配
    result = cv2.matchTemplate(gray, template_img, cv2.TM_CCORR_NORMED, mask=alpha)
    return img, template_img, result


def target_identification(img_path: str, window_title: str) -> tuple[float, float]:
    """ 模板图片 截图识别位置 返回中心点坐标 """
    img, template_img, result = template_matching(img_path, window_title)
    # 获取最大值和最小值以及他们的坐标
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # 返回中心点坐标
    h, w = template_img.shape[:2]
    return max_loc[0] + w / 2, max_loc[1] + h / 2


def target_identification_all(img_path: str, window_title: str, accuracy: float) -> list[tuple[float, float]]:
    """ 模板图片 截图识别位置 返回所有大于置信值中心点坐标 """
    loc_pos = []
    img = capture(window_title)
    template_img = cv2.imread(img_path)
    h, w = img.shape[:2]
    # 使用 TM_CCO-EFF_NORMED 算法寻找图片 最相似为 1 范围 0 ~ 1
    result = cv2.matchTemplate(img, template_img, cv2.TM_CCOEFF_NORMED)
    # 筛选对比度大于预期的全部值
    location = where(result >= accuracy)
    ex, ey = 0, 0
    for pt in zip(*location[::-1]):
        x = pt[0]
        y = pt[1]
        if (x - ex) + (y - ey) < 15:  # 去掉邻近重复的点
            continue
        ex, ey = x, y
        loc_pos.append((x + w / 2, y + h / 2))
    return loc_pos


__all__ = ['window_foreground', 'screen', 'capture', 'template_matching', 'target_identification',
           'continuous_screen', 'video_screen', 'target_identification_all']
