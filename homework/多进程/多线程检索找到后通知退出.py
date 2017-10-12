import threading
import os
class Find(threading.Thread):
    def __init__(self,kaifanglist,istart,iend,searchstr):
        threading.Thread.__init__(self)
        self.kaifanglist=kaifanglist
        self.istart=istart
        self.iend=iend
        self.searchstr=searchstr

        pass
    def run(self):
        print(self.getName(),"start")
        for i in range(self.istart,self.iend):
            global isfind
            if isfind:
                break
            line=self.kaifanglist[i].decode("gbk","ignore")
            if isfind and line.find(self.searchstr)!=-1:
                print(self.getName(),line,end="")
                isfind=True
                break
        print(self.getName(),"end")
isfind=False

path="F:\\大数据\\kaifangX.txt"
file=open(path,"rb")
kaifanglist=file.readlines()
lines=len(kaifanglist)
searchstr=input("输入要查询的数据")
N=10
threadlist=[]
for i in range(0,N-1):
    mythd=Find(kaifanglist,i*(lines//(N-1)),(i+1)*(lines//(N-1)),searchstr)
    mythd.start()
    threadlist.append(mythd)

mylastthd=mythd=Find(kaifanglist,lines-lines//(N-1)*(N-1),lines,searchstr)
mylastthd.start()
threadlist.append(mylastthd)
for thd in threadlist:
    thd.join()
print("finish")

finddata=Find(kaifanglist,0,len(kaifanglist),searchstr)
finddata.start()
finddata.join()
print("完工")

