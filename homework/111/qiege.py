#import os
#os.mkdir(r"C:\Users\Tsinghua-yincheng\Desktop\切割归并\split") #创建文件夹


num=10
filesplitlist=[] #文件集合
for  i   in  range(num):
    filepath=r"D:\朱烜宇\Bigdata\data"+str(i+1)+".txt"
    file=open(filepath,"wb")
    filesplitlist.append(file)

fileallpath=r"D:\朱烜宇\Bigdata\cred.txt" #归并
fileall=open(fileallpath,"rb")#写入
i=0
for  line  in fileall:
    filesplitlist[i%num].write(line)
    i+=1
    #print(line)
fileall.close()
for  i   in  range(num):
    filesplitlist[i].close()#关闭文件
