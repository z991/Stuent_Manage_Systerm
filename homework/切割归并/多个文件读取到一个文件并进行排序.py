import os
#os.listdir遍历所有文件或者文件夹。
#返回list
#print(os.listdir(r"Z:\F\第一阶段视频\20170531\52G葫芦娃\163mail1\163mail1"))
filepath="H:\\大数据\\邮箱\\163mail1切割\\111切割" #路径
filelist=os.listdir(filepath) #返回list包含所有文件名
fileallpath="H:\\大数据\\邮箱\\163mail1切割\\zong.txt" #归并
fileall=open(fileallpath,"wb")#写入
for   filename  in  filelist: #循环每一个文件名
    filelitepath=filepath+"\\"+filename  #路径

    filer= open(filelitepath,"rb")  #读取
    mylist = filer.readlines()  # 读取所有
    mylist.sort()
    for  line  in mylist:    #每一行地区之后写入
        fileall.write(line)
filer.close() #关闭
fileall.close()