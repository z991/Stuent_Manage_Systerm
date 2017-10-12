#func=lambda     :print("hello world")
#func()

import operator
file=open(r"D:\朱烜宇\大数据相关数据\data\csdnpasswordtimes.txt","rb")
mylist=file.readlines()
file.close()

newlist=[]



for line in mylist:
    line=line.decode("utf-8")
    linelist=line.split(' ')
    newlist.append(linelist)


newlist.sort(key=lambda X:int(X[0]))
newlist.reverse()

savefilepath=r"D:\朱烜宇\大数据相关数据\data\csdnpasswordsortlast.txt"
savefile=open(savefilepath,"wb")
for data in newlist:
    savefile.write((data[0]+" "+data[1]).encode("utf-8"))


savefile.close
print("save finish")