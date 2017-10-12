filepath=r"F:\大数据\Myspace.com\Myspace1.txt"
file=open(filepath,"rb")

saveyxfilepath=r"F:\大数据\Myspace.com\提取\Myspcelyx.txt"
saveqtfilepath=r"F:\大数据\Myspace.com\提取\Myspcelqt.txt"
saveyxfile=open(saveyxfilepath,"wb")
saveqtfile=open(saveqtfilepath,"wb")
print("start")
for  line in  file: #遍历数据的每一行
    #print(line)#字符串
    linstr=line.decode("gbk","ignore") #解码
    mylist=linstr.split(":")
    #print(mylist[2],end="")#打印
    if len(mylist)<2:
        saveqtfile.write(line)
    else:
        saveyxfile.write((mylist[1]+"\r\n").encode("utf-8"))
print("end")
saveqtfile.close()
saveyxfile.close()
file.close()