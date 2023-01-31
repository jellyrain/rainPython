import cv2, tkinter, os, time
import tkinter.simpledialog
from android.cores import watch, slide, click
from android.api import screen_capture


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

def capturemark(deviceID, action: int = 1, save_file_path: str = 'img/', pos_img_dict: str = 'img/dict.py',  scale: float = 0.5):
    """
    截图工具 
    action: 动作类型 1=截图  2=标点  3=标线（取起终点组成向量） 4=标记区域
    
    scale: 原图缩放比例，用于展示在窗口里
    
    save_file_path: 截图保存路径，以 '/' 结束
    pos_img_dict: py变量字典文件
    """

    # 图片来源替换输入你的did
    screen_capture(deviceID, "img/screen.png")
    img_file = "img/screen.png"


    # ===================================================
    # 以下部分可以不改动

    if not os.path.exists(save_file_path): 
        os.makedirs(save_file_path)
        time.sleep(1)

    def isVarExist(varName):
        if os.path.exists(pos_img_dict):
            with open(pos_img_dict, 'r', encoding='utf-8') as f:
                str = f.read()
                if varName in str:
                    return True
                else:
                    return False
        else:
            return False


    # type=动作类型 1=截图  2=标点  3=标线（取起终点组成向量） 4=标记区域
    def createVar(varName, value, type):
        with open(pos_img_dict, 'a+', encoding='utf-8') as f:
            if type == 1:
                f.write(varName + " = \"" + value + "\"\n")
            elif type == 2:
                f.write(varName + " = " + str(value) + "\n")
            elif type == 3:
                f.write(varName + " = " + str(value) + "\n")
            elif type == 4:
                f.write(varName + " = " + str(value) + "\n")

    def draw_Rect(event, x, y, flags, param):
        global drawing, startPos, stopPos
        if event == cv2.EVENT_LBUTTONDOWN:  # 响应鼠标按下
            drawing = True
            startPos = (x, y)
        elif event == cv2.EVENT_MOUSEMOVE:  # 响应鼠标移动
            if drawing == True:
                img = img_source.copy()
                cv2.rectangle(img, startPos, (x, y), (0, 255, 0), 2)
                cv2.imshow('image', img)
        elif event == cv2.EVENT_LBUTTONUP:  # 响应鼠标松开
            drawing = False
            stopPos = (x, y)
        elif event == cv2.EVENT_RBUTTONUP:
            if startPos == (0, 0) and stopPos == (0, 0):
                return
            x0, y0 = startPos
            x1, y1 = stopPos
            cropped = img_source[y0:y1, x0:x1]  # 裁剪坐标为[y0:y1, x0:x1]
            res = tkinter.simpledialog.askstring(title="输入", prompt="请输入图片变量名：（存储路径为" + save_file_path + "）",
                                                initialvalue="")
            if res is not None:
                if isVarExist(res):
                    tkinter.simpledialog.messagebox.showerror("错误", "该变量名已存在，请更换一个或手动去文件中删除！")
                else:
                    cv2.imwrite(save_file_path + res + ".png", cropped)
                    createVar(res, save_file_path + res + ".png", 1)
                    tkinter.simpledialog.messagebox.showinfo("提示", "创建完成！")
        elif event == cv2.EVENT_MBUTTONUP:
            if startPos == (0, 0) and stopPos == (0, 0):
                return
            x0, y0 = startPos
            x1, y1 = stopPos
            cropped = img_source[y0:y1, x0:x1]  # 裁剪坐标为[y0:y1, x0:x1]
            cv2.imshow('cropImage', cropped)
            cv2.waitKey(0)


    def draw_Point(event, x, y, flags, param):
        global drawing, startPos, stopPos
        if event == cv2.EVENT_LBUTTONDOWN:  # 响应鼠标按下
            drawing = True
            startPos = (x, y)
            img = img_source.copy()
            cv2.circle(img, startPos, 2, (0, 255, 0), 2)
            cv2.putText(img, "Point:" + str(startPos), (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0, 255, 0), 3)
            print("Point:" + str(startPos))
            cv2.imshow('image', img)
        elif event == cv2.EVENT_RBUTTONUP:
            if startPos == (0, 0):
                return
            res = tkinter.simpledialog.askstring(title="输入", prompt="请输入坐标 " + str(startPos) + " 变量名：", initialvalue="")
            if res is not None:
                if isVarExist(res):
                    tkinter.simpledialog.messagebox.showerror("错误", "该变量名已存在，请更换一个或手动去文件中删除！")
                else:
                    createVar(res, startPos, 2)
                    tkinter.simpledialog.messagebox.showinfo("提示", "创建完成！")


    def draw_Line(event, x, y, flags, param):
        global drawing, startPos, stopPos
        if event == cv2.EVENT_LBUTTONDOWN:  # 响应鼠标按下
            drawing = True
            startPos = (x, y)
        elif event == cv2.EVENT_MOUSEMOVE:  # 响应鼠标移动
            if drawing == True:
                img = img_source.copy()
                cv2.line(img, startPos, (x, y), (0, 255, 0), 2)
                cv2.imshow('image', img)
        elif event == cv2.EVENT_LBUTTONUP:  # 响应鼠标松开
            drawing = False
            stopPos = (x, y)
            print("startPoint:" + str(startPos) + " stopPoint:" + str(stopPos))
        elif event == cv2.EVENT_RBUTTONUP:
            if startPos == (0, 0) and stopPos == (0, 0):
                return
            res = tkinter.simpledialog.askstring(title="输入", prompt="请输入开始坐标 " + str(startPos) + " 到结束坐标 " + str(
                stopPos) + " 组成向量的变量名：", initialvalue="")
            if res is not None:
                if isVarExist(res):
                    tkinter.simpledialog.messagebox.showerror("错误", "该变量名已存在，请更换一个或手动去文件中删除！")
                else:
                    createVar(res, (startPos, stopPos), 3)
                    tkinter.simpledialog.messagebox.showinfo("提示", "创建完成！")


    def draw_Rect_Pos(event, x, y, flags, param):
        global drawing, startPos, stopPos
        if event == cv2.EVENT_LBUTTONDOWN:  # 响应鼠标按下
            drawing = True
            startPos = (x, y)
        elif event == cv2.EVENT_MOUSEMOVE:  # 响应鼠标移动
            if drawing == True:
                img = img_source.copy()
                cv2.rectangle(img, startPos, (x, y), (0, 255, 0), 2)
                cv2.imshow('image', img)
        elif event == cv2.EVENT_LBUTTONUP:  # 响应鼠标松开
            drawing = False
            stopPos = (x, y)
            print("startPoint:" + str(startPos) + " stopPoint:" + str(stopPos))
        elif event == cv2.EVENT_RBUTTONUP:
            if startPos == (0, 0) and stopPos == (0, 0):
                return
            x0, y0 = startPos
            x1, y1 = stopPos
            res = tkinter.simpledialog.askstring(title="输入", prompt="请输入矩形范围变量名：",
                                                initialvalue="")
            if res is not None:
                if isVarExist(res):
                    tkinter.simpledialog.messagebox.showerror("错误", "该变量名已存在，请更换一个或手动去文件中删除！")
                else:
                    createVar(res, (startPos, stopPos), 4)
                    tkinter.simpledialog.messagebox.showinfo("提示", "创建完成！")
        elif event == cv2.EVENT_MBUTTONUP:
            if startPos == (0, 0) and stopPos == (0, 0):
                return
            x0, y0 = startPos
            x1, y1 = stopPos
            cropped = img_source[y0:y1, x0:x1]  # 裁剪坐标为[y0:y1, x0:x1]
            cv2.imshow('cropImage', cropped)
            cv2.waitKey(0)

    drawing = False
    startPos = (0, 0)
    stopPos = (0, 0)
    img_source = cv2.imread(img_file)
    img = img_source.copy()

    root = tkinter.Tk()
    root.title('dialog')
    root.resizable(0, 0)
    root.withdraw()

    h_src, w_src, tongdao = img.shape
    w = int(w_src * scale)
    h = int(h_src * scale)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.resizeWindow("image", w, h)
    if action == 1:
        cv2.setMouseCallback('image', draw_Rect)
    elif action == 2:
        cv2.setMouseCallback('image', draw_Point)
    elif action == 3:
        cv2.setMouseCallback('image', draw_Line)
    elif action == 4:
        cv2.setMouseCallback('image', draw_Rect_Pos)

    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    root.destroy()
    if os.path.exists(img_file): os.remove(img_file)

__all__ = ['watch_and_click', 'img_and_slide', 'watch_not_slide', 'watch_not_slide_and_client', 'capturemark']
