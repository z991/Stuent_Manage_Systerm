import codecs
filepath=r"D:\朱烜宇\Bigdata\尚客优酒店会员.sql"
file=codecs.open(filepath,"rb","gbk","ignore")#按照指定编码
mylist=file.readlines()#返回一个list,读取到内存
file.close()

savegoodfilepath=r"D:\朱烜宇\Bigdata\data\尚客优酒店会员good18.SQL"
savebadfilepath=r"D:\朱烜宇\Bigdata\data\尚客优酒店会员bad.SQL"
filegood=open(savegoodfilepath,"wb")
filebad=open(savebadfilepath,"wb")
for  line  in  mylist:
    linelist=line.split(",")
    if  len(linelist)>=13:
        if len(linelist[12])==18:
            #good
            filegood.write(line.encode("gbk"))
            pass
        else:
            #bad
            filebad.write(line.encode("gbk"))
            pass
    else:
        #bad
        filebad.write(line.encode("gbk"))
        pass


filebad.close()
filegood.close()
