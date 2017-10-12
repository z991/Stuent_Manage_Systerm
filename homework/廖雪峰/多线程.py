import time,threading
def loop():
    print('thread %s is running...'% threading.current_thread().name)
    n=0
    while n<5:
        n=n+1
        print('thread %s >>>%s')