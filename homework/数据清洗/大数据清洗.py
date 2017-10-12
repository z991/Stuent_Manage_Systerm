import codecs
filepath=r"D:\朱烜宇\大数据相关数据\1E01.txt"
file=codecs.open(filepath,"rb","gbk","ignore")
mylist=file.readlines()
savegoodfilepath=r"D:\朱烜宇\大数据相关数据\data1E01\1E01good.txt"
savebadfilepath=r"D:\朱烜宇\大数据相关数据\data1E01\1E01bad.txt"

filegood=open(savegoodfilepath)
filebad=open(savebadfilepath)
print("start")
for line in mylist:

    if len(line)>35 or len(line)<15:
        filebad.write(line.encode("utf-8"))
    else:
        QQlist = line.split('----')
        if  len(QQlist)==2:
            filegood.write(line.encode("utf-8"))
        else:
            filebad.write(line.encode("utf-8"))
print("end")
filebad.close()
filegood.close