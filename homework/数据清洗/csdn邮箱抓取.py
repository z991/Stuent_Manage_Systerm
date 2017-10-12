filepath=r"D:\朱烜宇\大数据相关数据\csdn.txt"
file=open(filepath,"rb")

savefilepath=r"D:\朱烜宇\大数据相关数据\data\csdn邮箱.txt"
savefile=open(savefilepath,"wb")
print("start")

for line in file:#遍历数据每一行
    #print(line)
    linstr=line.decode("gbk","ignore")
    mylist=linstr.split(" # ")
    #print(mylist[2],end="")
    savefile.write((mylist[2]+"\r\n").encode("utf-8"))
print("end")
savefile.close()
file.close()