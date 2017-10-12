import re

#获取邮件地址主要就是依靠强大的正则表达式

mailre = re.compile("[a-zA-Z0-9_.-]+@[a-zA-Z0-9_.-]+")

filepath=r"F:\大数据\51cto.txt"
file=open(filepath,"rb")


line = file.read()

linstr=line.decode("gbk","ignore")
mylist=(mailre.findall(linstr))

file = open(r"F:\大数据\51cto\51cto邮箱正则.txt", "wb")
if mylist != None:
    for mail in mylist:
        file.write((mail + "\r\n").encode("utf-8"))