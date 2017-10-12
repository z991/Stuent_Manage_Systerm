import urllib
import urllib.request
import threading
import time

def getstock(i):
    url = "http://hq.sinajs.cn/list=sz300" + str(i)
    print(urllib.request.urlopen(url).read().decode("gbk"))
while True:
    time.sleep(1)
    threadlist=[]
    for i in range(100,150):
        th=threading.Thread(target=getattr,args=(i,))
        th.start()
        threadlist.append(th)
    for th in threadlist:
        th.join()
    print("完成")
