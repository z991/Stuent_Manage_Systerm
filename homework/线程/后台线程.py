import threading
import time
import win32api

class Mythread(threading.Thread):
    def run(self):
        win32api.MessageBox(0,"帅帅朱你好","来自402帝国的问候",1)
mythread=[]
for i in range(5):
    t=Mythread()
    #t.setDaemon(True)
    t.start()
    mythread.append(t)
#threading.Thread默认是前台进程，主进程必须等前台
print("game over")