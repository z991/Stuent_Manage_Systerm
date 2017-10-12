filepath=r"D:\朱烜宇\大数据相关数据\data\csdnpassword.txt"
file=open(filepath,"rb")
mylist=file.readlines()#读取所有
mylist.sort()
file.close()


print("sort finish")
savefilepath=r"D:\朱烜宇\大数据相关数据\data\csdnpasswordsort.txt"
savefile=open(savefilepath,"wb")
for line in mylist:
    savefile.write(line)


savefile.close
print("save finish")