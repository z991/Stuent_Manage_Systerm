filepath=r"D:\朱烜宇\大数据相关数据\1E01.txt"
file=open(filepath,"rb")

savefilepath=r"D:\朱烜宇\大数据相关数据\dataQQ\1E01password.txt"
savefile=open(savefilepath,"wb")
print("start")
for  line in  file: #遍历数据的每一行
    #print(line)#字符串
    linstr=line.decode("gbk","ignore") #解码
    mylist=linstr.split("----")
    #print(mylist[2],end="")#打印
    savefile.write((mylist[1]+"\r\n").encode("utf-8"))
print("end")
savefile.close()
file.close()