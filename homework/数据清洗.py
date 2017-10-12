import codecs
filepath=r"F:\大数据\邮箱\163mail1切割\163mail111.txt"
file=codecs.open(filepath,"rb","gbk","ignore")
mylist=file.readlines()
savegoodfilepath=r"F:\大数据\邮箱\163mail1切割\清洗\163mail11good.txt"
savebadfilepath=r"F:\大数据\邮箱\163mail1切割\清洗\163mail11bad.txt"

filegood=open(savegoodfilepath,"wb")
filebad=open(savebadfilepath,"wb")
print("start")
for line in mylist:

    if len(line)<24:
        filebad.write(line.encode("utf-8"))
    else:
        emaillist = line.split('----')
        if  len(emaillist)>=2:
            filegood.write(line.encode("utf-8"))
        else:
            filebad.write(line.encode("utf-8"))
print("end")
filebad.close()
filegood.close