import codecs
filepath=r"D:\朱烜宇\大数据相关数据\uuu9.com.sql"
file=codecs.open(filepath,"rb","gbk","ignore")
mylist=file.readlines()

file.close
savefilepath=r"D:\朱烜宇\大数据相关数据\data\uuu9.com邮箱.sql"
savefile=open(savefilepath,"wb")


for line in mylist:
    linelist=line.split(" ")
    if len(linelist)<3:
        savefile.write((linelist[2] + "\r\n").encode("utf-8"))
    else:
        savefile.write((linelist[2] + "\r\n").encode("utf-8"))




file.close()
