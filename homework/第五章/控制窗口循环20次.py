import win32gui
import win32con
import time
import math
QQ=win32gui.FindWindow("TXGuiFoundation","QQ")
num=0
while num<20:
    num=num+1
    for  size  in  range(0,800,1):#向右
        win32gui.SetWindowPos(QQ,  #操作记事本
                          win32con.HWND_TOPMOST, #最上方
                          size, #位置x
                          0,#位置y
                          300,#长度
                          300,#宽度
                          win32con.SWP_SHOWWINDOW)
    for  size  in  range(0,600,1):#向下
        win32gui.SetWindowPos(QQ,  #操作记事本
                          win32con.HWND_TOPMOST, #最上方
                          800, #位置x
                          size,#位置y
                          300,#长度
                          300,#宽度
                          win32con.SWP_SHOWWINDOW)
    for  size  in  range(800,0,-1):#向左
        win32gui.SetWindowPos(QQ,  #操作记事本
                          win32con.HWND_TOPMOST, #最上方
                          size, #位置x
                          600,#位置y
                          300,#长度
                          300,#宽度
                          win32con.SWP_SHOWWINDOW)
    for size in range(600, 0, -1):#向上
        win32gui.SetWindowPos(QQ,  # 操作记事本
                              win32con.HWND_TOPMOST,  # 最上方
                              0,  # 位置x
                              size,#置y
                              300,  # 长度
                              300,  # 宽度
                              win32con.SWP_SHOWWINDOW)