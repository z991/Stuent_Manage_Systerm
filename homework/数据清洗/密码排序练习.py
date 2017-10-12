filepath=r"D:\朱烜宇\大数据相关数据\dataQQ\1E01password.txt"
file=open(filepath,"rb")
mylist=file.readlines() #读取所有
mylist.sort()#排序
file.close()

print("sort ")
savefilepath=r"D:\朱烜宇\大数据相关数据\dataQQ\1E01passwordsort.txt"
savefile=open(savefilepath,"wb")
for  line in  mylist:
    savefile.write(line)
savefile.close()
print("save ")