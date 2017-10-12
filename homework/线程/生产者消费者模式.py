import threading
import queue
import time
import random

class creatorThread(threading.Thread):
    def __init__(self,index,myqueue):
        threading.Thread.__init__(self)
        self.index=index
        self.myqueue=myqueue
    def run(self):
        while True:
            time.sleep(3)
            num=random.randint(1,100000)
            self.myqueue.put("input 生产者"+str(self.index)+"核桃"+str(num))
        self.myqueue.task_done()

class buyerThread(threading.Thread):
    def __init__(self,index,myqueue):
        threading.Thread.__init__(self)
        self.index=index
        self.myqueue=myqueue
    def run(self):
        while True:
            time.sleep(1)
            item=self.myqueue.get()
            if item is None:
                break
            print("客户",self.index,"买到物品",item)
        self.myqueue.task_done()

myqueue=queue.Queue(10)
for i in range(3):
    creatorThread(i,myqueue).start()
for i in range(8):
    buyerThread(i,myqueue).start()