import operator
file =open(r"D:\朱烜宇\大数据相关数据\datacdsn\csdnpasswordsorttimes.txt","rb")
mylist=file.readlines() #读取内存
file.close()


newlist=[] #存储账户密码与次数
for  line in mylist:
    line=line.decode("utf-8")#二进制转化为文本
    linelist=line.split(' ')#文本的切糕
    newlist.append(linelist)
#[["1","12321"],["2"，"123213"]]
#newlist.sort(key=operator.itemgetter(0)) #根据第一个排序
newlist.sort(key=lambda x:int(x[0])) #次数转化为整数排序  x=["1","12321"]
newlist.reverse()#反转


savefilepath=r"D:\朱烜宇\大数据相关数据\datacdsn\csdnpasswordsortlast2.txt"
savefile=open(savefilepath,"wb")
for data  in newlist:
    savefile.write((data[0]+" "+data[1]).encode("utf-8"))
savefile.close()
print("save ")