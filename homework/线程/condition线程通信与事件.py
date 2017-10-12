import threading
import time

def go1():
    with cond:
        for i in range(10):
            time.sleep(1)
            print(threading.current_thread().name,i)
            if i==5:
                cond.wait()
def go2():
    with cond:
        for i in range(10):
            time.sleep(1)
            print(threading.current_thread().name,i)
        cond.notify()
cond=threading.Condition()
threading.Thread(target=go1).start()
threading.Thread(target=go2).start()