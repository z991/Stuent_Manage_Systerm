import codecs
filepath=r"D:\朱烜宇\大数据相关数据\uuu9.com.sql"
file=codecs.open(filepath,"rb","gbk","ignore")
mylist=file.readlines()

file.close
savegoodfilepath=r"D:\朱烜宇\大数据相关数据\data\uuu9.comgood.sql"
savebadfilepath=r"D:\朱烜宇\大数据相关数据\data\uuu9.combad.sql"
filegood=open(savegoodfilepath,"wb")
filebad=open(savebadfilepath,"wb")
for line in mylist:
    linelist=line.split(" | ")
    if len(linelist)>=2:
        filegood.write(line.encode("utf-8"))

    else:
        filebad.write(line.encode("utf-8"))

filebad.close()
filegood.close()