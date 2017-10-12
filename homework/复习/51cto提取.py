filepath=r"F:\大数据\51cto.txt"
file=open(filepath,"rb")

saveyxfilepath=r"F:\大数据\51cto\51cto邮箱.txt"
savezhfilepath=r"F:\大数据\51cto\51cto账号.txt"
saveqtfilepath=r"F:\大数据\51cto\51cto其他.txt"
saveyxfile=open(saveyxfilepath,"wb")
savezhfile=open(savezhfilepath,"wb")
saveqtfile=open(saveqtfilepath,"wb")
print("start")
for  line in  file: #遍历数据的每一行
    #print(line)#字符串
    linstr=line.decode("gbk","ignore") #解码
    mylist=linstr.split(";")
    #print(mylist[2],end="")#打印
    if len(mylist)==3:
        saveyxfile.write((mylist[-1]).encode("utf-8"))
        savezhfile.write((mylist[1] + "\r\n").encode("utf-8"))
    else:
        saveqtfile.write(line)
print("end")
saveqtfile.close()
saveyxfile.close()
savezhfile.close()
file.close()

