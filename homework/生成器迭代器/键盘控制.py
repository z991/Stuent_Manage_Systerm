import win32con
import win32api
import time
win32api.keybd_event(87,0,0,0) #键盘按下   向前（W）
time.sleep(0.1)
win32api.keybd_event(87,0,win32con.KEYEVENTF_KEYUP,0)#键盘松开


win32api.keybd_event(65,0,0,0) #键盘按下   向左（A）
time.sleep(0.1)
win32api.keybd_event(65,0,win32con.KEYEVENTF_KEYUP,0)#键盘松开

win32api.keybd_event(68,0,0,0) #键盘按下   向右（D）
time.sleep(0.1)
win32api.keybd_event(68,0,win32con.KEYEVENTF_KEYUP,0)#键盘松开

win32api.keybd_event(83,0,0,0) #键盘按下   向后（S）
time.sleep(0.1)
win32api.keybd_event(83,0,win32con.KEYEVENTF_KEYUP,0)#键盘松开

#6：剑
#乱草 A
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)

#巧篆 A A
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
time.sleep(0.1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
#重隶 A A A
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
time.sleep(0.1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
time.sleep(0.1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
#残日红江 ↑A

#残泉回春 ↓A
#风残草尽 ↓A↓A
#烛举焰残 ←A (破防)
#枯鹰残木 →A
#雀置喙 ↓↓A (破防)
#鹤舒翎 ↓↑A
#孤雁回 ↓↑A↓↑A
#燕双飞 ↑↓A
#忌夏日 ↑↑A
#忌秋风 ↑↑A↑↑A
#忌冬雨 ↓↑↑A
#凤凰雏 ←→A(需60%气)
#血残气丧 →←A(需60%气)
#凤凰羽 ←→↑A (破防，需100%气)
#轻行 A(空中)
#正楷 A A(空中)
#刻铭 ↓A(空中)