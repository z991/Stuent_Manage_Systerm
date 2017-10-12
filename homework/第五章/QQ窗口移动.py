import win32gui
import win32con
import time

'''
notepad=win32gui.FindWindow("Notepad","无标题 - 记事本")
for  i  in  range(10):
    for  size  in  range(0,800,10):
        win32gui.SetWindowPos(notepad,  #操作记事本
                          win32con.HWND_TOPMOST, #最上方
                          0, #位置x
                          0,#位置y
                          size,#长度
                          size,#宽度
                          win32con.SWP_SHOWWINDOW)
    for  size  in  range(800,0,-10):
        win32gui.SetWindowPos(notepad,  #操作记事本
                          win32con.HWND_TOPMOST, #最上方
                          0, #位置x
                          0,#位置y
                          size,#长度
                          size,#宽度
                          win32con.SWP_SHOWWINDOW)

'''


QQ=win32gui.FindWindow("TXGuiFoundation","QQ")
while True:
    for  size  in  range(0,800,10):
        win32gui.SetWindowPos(QQ,  #操作记事本
                          win32con.HWND_TOPMOST, #最上方
                          size, #位置x
                          0,#位置y
                          300,#长度
                          300,#宽度
                          win32con.SWP_SHOWWINDOW)
    for  size  in  range(800,0,-10):
        win32gui.SetWindowPos(QQ,  #操作记事本
                          win32con.HWND_TOPMOST, #最上方
                          size, #位置x
                          0,#位置y
                          300,#长度
                          300,#宽度
                          win32con.SWP_SHOWWINDOW)