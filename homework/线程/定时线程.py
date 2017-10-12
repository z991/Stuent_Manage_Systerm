import time
import os
import threading

def go():
    while True:
        time.sleep(3)
        os.system("calc")
timethread=threading.Timer(5,go)
timethread.start()
i=0
while True:
    time.sleep(1)
    print(i)
    i+=1