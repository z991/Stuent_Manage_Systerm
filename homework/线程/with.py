import threading
import time
num=0
mutex=threading.Lock()
class Mythread(threading.Thread):
    def run(self):
        global num
        with mutex:
            for i in range(100000):
                num+=1
        print(num)

mythread=[]
for i in range(5):
    t=Mythread()
    t.start()
    mythread.append(t)
for i in mythread:
    t.join()
print("game over")

''' with mutex:
            for i in range(100000):
                num+=1
    if mutex.acquire(1):
        for i in range(100000):
            num+=1
        mutex.rlease()'''