import csv
import threading
import queue
import os
class getdatatotal(threading.Thread):
    def __init__(self,path,queue):
        threading.Thread.__init__(self)
        self.path=path
        self.queue=queue
    def run(self):
        print(self.getName())
        reader=csv.reader(open(self.path,"r"))
        num=0
        alldata=0
        for item in reader:
            if num==0:
                pass
            else:
                alldata+=eval(item[13])
            num+=1
        print(alldata/num,self.getName())
        self.queue.put(alldata/num)
myqueue=queue.Queue(0)
path="H:\\DAY\\day23down\\csv"
filelist=os.listdir(path)
filepathlist=[]
for filename in filelist:
    filename=path+"\\"+filename
    filepathlist.append(filename)
threadlist=[]
for path in filepathlist:
    mythread=getdatatotal(path,myqueue)
    mythread.start()
for thread in threadlist:
    thread.join()
while not myqueue.empty():
    data=myqueue.get()
    print(data)