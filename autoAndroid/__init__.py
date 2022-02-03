from autoAndroid.api import connectAdb, getDevices, killAdb
from autoAndroid.implementation  import *

class Carriers:
   # 初始化
   def __init__(self, deviceID):
      self.deviceID = deviceID
   
   # ADB 连接设备
   @staticmethod
   def connectAdb(deviceID):
      print(connectAdb(deviceID))

   # 获取设备列表，每一个为 deviceID 并且 打印结果
   @staticmethod
   def getDevices():
      print(getDevices())

   # 杀死ADB进程 并且 打印结果
   @staticmethod
   def killAdb():
      print(killAdb())

   # 点击指定坐标位置
   def touch(self, x, y):
      click(self.deviceID, x, y)

   # 监听图片出现 并且 返回图片所在区块的中心坐标
   def watch(self, imgPath, duration = 60 ,intervalTime = 1, threshold = 0.7):
      return watch(self.deviceID, imgPath, duration, intervalTime, threshold)

   # 长按点击
   def longTouche(self, x, y, second = 3):
      longClick(self.deviceID, x, y, second)

   # 滑动操作
   def slide(self,  x1, y1, x2, y2, second = 1):
      slide(self.deviceID, x1, y1, x2, y2, second)

   # 监听图片出现 并且 点击
   def watchAndTouche(self, imgPath, duration = 60 ,intervalTime = 1, threshold = 0.7):
      watchAndClick(self.deviceID, imgPath, duration ,intervalTime, threshold)
   
   # 根据两张图片滑动操作 两个点都是 图片中心点
   def imgAndSlide(self, imgPath1, imgPath2, second = 1, threshold = 0.7):
      imgAndSlide(self.deviceID, imgPath1, imgPath2, second, threshold)

   # 监听图片出现 未出现 滑动 出现 返回图片所在区块的中心坐标
   def watchNotSlide(self, imgPath, x1, y1, x2, y2, second = 1, maxnumber = 20, threshold = 0.7):
      return watchNotSlide(self.deviceID, imgPath, x1, y1, x2, y2, second, maxnumber, threshold)

   # 监听图片出现 未出现 滑动 出现 点击
   def watchNotSlideAndTouche(self, imgPath, x1, y1, x2, y2, second = 1, maxnumber = 20, threshold = 0.7):
      watchNotSlideAndClient(self.deviceID, imgPath, x1, y1, x2, y2, second, maxnumber, threshold)

   # 监听多张图片是否出现 出现一张就返回 或运算
   def watchOrImgs(self, imgPaths, duration = 60 ,intervalTime = 1, threshold = 0.7):
      return watchOrImgs(self.deviceID, imgPaths, duration, intervalTime, threshold)

   # 等待
   def sleep(self, second = 1):
      sleep(second)

   # 随机等待
   def randomSleep(self, endSecond = 2, startSecond = 0):
      randomSleep(endSecond, startSecond)

   # 修改 device
   def deviceID(self, deviceID):
      self.deviceID = deviceID
      print(connectAdb(self.deviceID))

__all__ = ['Carriers']