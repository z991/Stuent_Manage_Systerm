import codecs
filepath=r"D:\朱烜宇\大数据相关数据\kaifangX.txt"
file=codecs.open(filepath,"rb","gbk","ignore")
mylist=file.readlines()

file.close
savegoodfilepath=r"D:\朱烜宇\大数据相关数据\开房\kaifanggood.txt"
savebadfilepath=r"D:\朱烜宇\大数据相关数据\开房\kaifangbad.txt"
filegood=open(savegoodfilepath,"wb")
filebad=open(savebadfilepath,"wb")
for line in mylist:
    linelist=line.split(",")
    if len(linelist)>=2:
        if len(linelist[1])==18:
            filegood.write(line.encode("utf-8"))
        else:
            filebad.write(line.encode("utf-8"))
    else:
        filebad.write(line.encode("utf-8"))

filebad.close()
filegood.close()