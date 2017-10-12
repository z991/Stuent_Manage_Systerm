'''import threading
from time import sleep,ctime
def loop(nsec):
    print("Start loop:(:>30)").format(ctime())
    print("Sleep {} seconds...".format(nsec))
    sleep(nsec)

def main():
    print("Starting:{:>30}",format(ctime()))
    t=threading.Thread(target=loop,args=(3,))
    t.start()
    t.join()
    print("All Done :{:>30}".format(ctime()))

if __name__=="__main__":
    main()
#coding=utf-8
import time
def saySorry():
    print("亲爱的，我错了，我能吃饭了吗？")
    time.sleep(1)
if __name__ == "__main__":
    for i in range(5):
        saySorry()'''

import threading
import time
import win32api

class Mythread(threading.Thread):
    def run(self):
        win32api.MessageBox(0,"你的账户很危险","来自支付宝",2)
mythread=[]
for i in range(5):
    t=Mythread()
    t.start()
    mythread.append(t)
