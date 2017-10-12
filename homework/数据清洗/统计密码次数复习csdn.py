filepath=r"D:\朱烜宇\大数据相关数据\data\csdnpasswordsort.txt"
file=open(filepath,"rb")
mylist=file.readlines()#读取所有
length=len(mylist)
file.close()


savefilepath=r"D:\朱烜宇\大数据相关数据\data\csdnpasswordtimes.txt"
savefile=open(savefilepath,"wb")

i=0
while i<length:
    times=1
    passwordstr=mylist[i]
    while i+1<=length-1 and mylist[i].decode("utf-8")==mylist[i+1].decode("utf-8"):
        times=times+1
        i=i+1
        savefile.write((str(times)+" "+passwordstr.decode("utf-8")).encode("utf-8"))



    i=i+1


savefile.close()
print("save")