import time
def getcosttime(go):
    starttime = time.time()
    go()
    endtime = time.time()
    print(endtime - starttime)


def go():
    lastnum=0
    for i in range(1,100000000):
        lastnum+=1
    print(lastnum)
def come():
    lastnum=0.0
    for i in range(1,100000000):
        lastnum+=1
    print(lastnum)

getcosttime(go)
getcosttime(come)