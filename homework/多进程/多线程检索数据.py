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
        for i in range(self.istart,self.iend):
            line=self.kaifanglist[i].decode("gbk","ignore")
            if line.find(self.searchstr)!=-1:
                print(line)
        pass
path="F:\\大数据\\kaifangX.txt"
file=open(path,"rb")
kaifanglist=file.readlines()
searchstr=input("输入要查询的数据")
finddata=Find(kaifanglist,0,len(kaifanglist),searchstr)
finddata.start()
finddata.join()
print("完工")


'''
path="F:\\大数据\\kaifangX.txt"
file=open(path,"rb")
kaifanglist=file.readlines()
searchstr=input("输入要查询的数据")
for line in kaifanglist:
    line=line.decode("gbk","ignore")
    if line.find(searchstr)!=-1:
        print(line)'''
