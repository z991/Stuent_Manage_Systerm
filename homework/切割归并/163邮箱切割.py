num=5
filesplitlist=[] #文件集合
for  i   in  range(num):
    filepath=r"H:\大数据\邮箱\163mail1切割\111切割"+str(i+1)+".txt"
    file=open(filepath,"wb")
    filesplitlist.append(file)

fileallpath=r"H:\大数据\邮箱\163mail1切割\163mail111.txt" #归并
fileall=open(fileallpath,"rb")#写入
i=0
for  line  in fileall:
    filesplitlist[i%num].write(line)
    i+=1
    #print(line)
fileall.close()
for  i   in  range(num):
    filesplitlist[i].close()#关闭文件
