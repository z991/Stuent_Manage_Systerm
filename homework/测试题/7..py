'''str1=input("请输入文件的位置及文件名")
str2=input("请输入要拷贝的位置及文件名")

filepath=r"str1"
file=open(filepath,"rb")

savefilepath=r"str2"
savefile=open(savefilepath,"wb")
savefile.close()
file.close()'''
import codecs
def loaddata():#加载数据

    filepath = r"D:\朱烜宇\大数据相关数据\1.txt"#路径
    file = codecs.open(filepath, "rb", "gbk", "ignore")#读取
    global datalist
    datalist=file.readlines()#读取文件到list
    file.close()
def search(namestr):
    savefilepath= "D:\\朱烜宇\\大数据相关数据\\data\\11.txt"
    savefile=open(savefilepath,"wb")
    for line in datalist:
            savefile.write(line.encode("utf-8"))




datalist=[]
print("star")
loaddata()
print("end")
