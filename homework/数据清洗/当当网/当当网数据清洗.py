filepath=r"D:\朱烜宇\大数据相关数据\dangdangwang.txt"
file=open(filepath,"rb")

savefilepath=r"D:\朱烜宇\大数据相关数据\datadangdang\dangdangwang邮箱.txt"
savefile=open(savefilepath,"wb")
print("start")
for  line in  file: #遍历数据的每一行
    #print(line)#字符串
    linstr=line.decode("gbk","ignore") #解码
    mylist=linstr.split(",")
    print(mylist[0])#打印
    savefile.write(mylist[0].encode("utf-8"))
print("end")
savefile.close()
file.close()