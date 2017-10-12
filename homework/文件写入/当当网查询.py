import codecs
def loaddata():
    filepath=r"D:\\朱烜宇\\大数据相关数据\\dangdangwang.txt"
    file=codecs.open(filepath,"rb",encoding="gbk",errors="ignore")
    global datalist
    datalist=file.readlines()
    file.close()
def search(namestr):
    savefilepath="D:\\朱烜宇\\大数据相关数据\\data\\"+namestr+".txt"
    savefile=open(savefilepath,"wb")
    numbers=0
    for line in datalist:
        if line.find(namestr)!=-1:
            print(line,end="")
            numbers +=1
            savefile.write(line.encode("utf-8"))
    savefile.write(("数量是"+str(numbers)).encode("utf-8"))
    savefile.close()


datalist=[]
print("load file start")
loaddata()
print("load file end")
while True:
    searchname=input("要查询的数据")
    search(searchname)
print(numbers)