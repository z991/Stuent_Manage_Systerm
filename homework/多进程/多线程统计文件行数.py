import threading
import csv
import os
class MyThreadLine(threading.Thread):#定义一个统计行数的类
    def __init__(self,path):
        threading.Thread.__init__(self)#父类初始化
        self.path=path#路径
        self.line=-1#行数
        pass
    def run(self):
        reader=csv.reader(open(self.path,"r"))#读取文件
        lines=0
        for item in reader:#读取每一行
            lines+=1
        self.line=lines#保存行数
        print(self.getName(),self.line)
        pass
'''path="D:\\朱烜宇\\day23down\\csv\\000001.csv"
mythd=MyThreadLine(path)
mythd.start()
mythd.join()
print(mythd.line)'''
path="D:\\朱烜宇\\day23down\\csv"
filelist=os.listdir(path)#存储所有的文件
threadlist=[]#线程列表
for filename in filelist:
    newpath=path+"\\"+filename#代表完整路径
    mythd=MyThreadLine(newpath)#创建线程类对象
    mythd.start()#线程开始干活
    threadlist.append(mythd)#增加线程到线程列表
for mythd in threadlist:#遍历每一个线程
    mythd.join()#等待所有线程干完活
linelist=[]
for mythd in threadlist:
    linelist.append(mythd.line)
print(linelist )


