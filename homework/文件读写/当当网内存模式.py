import codecs
def loaddata():#加载数据

    filepath = r"D:\朱烜宇\大数据相关数据\dangdangwang.txt"#路径
    file = codecs.open(filepath, "rb", "gbk", "ignore")#读取
    global datalist
    datalist=file.readlines()#读取文件到list
    file.close()
def search(namestr):
    savefilepath= "D:\\朱烜宇\\大数据相关数据\\data\\"+namestr+".txt"
    savefile=open(savefilepath,"wb")
    for line in datalist:
        if line.find(namestr)!=-1:
            print(line,end="")
            savefile.write(line.encode("utf-8"))




datalist=[]
print("star")
loaddata()
print("end")
while True:
    searchname=input("查询的数据")
    search(searchname)
