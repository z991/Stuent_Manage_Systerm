import  os
import multiprocessing
import time
import csv

def getline(path,mylist):
    reader = csv.reader(open(path, "r"))  # 读取文件
    lines = 0
    for item in reader:  # 读取每一行
        lines += 1
    print("self pid", os.getpid(),"lines",lines)
    mylist.append(lines) #增加数据



if  __name__=="__main__":
    path = "D:\朱烜宇\day23down\csv"
    filelist = os.listdir(path)  # 存储了所有的文件名
    processlist = []  # 进程列表
    mylist = multiprocessing.Manager().list() #共享list,共享内存

    for  filename  in filelist:
        newpath=path+"\\"+filename #代表完整路径
        p=multiprocessing.Process(target=getline,args=(   newpath,mylist))#开启进程
        p.start() #进程开始干活
        processlist.append(p) #加入进程列表

    for  mythd in processlist:#遍历每一个进程
        mythd.join() #等待所有进程干完活
    print(mylist)
    print("完成")


