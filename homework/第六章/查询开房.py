#print("hello".find("el"))
#print("hello".find("ak"))
import codecs
#第一个参数路径，第二个参数，rb二进制读写，第三个 汉子编码，第四个忽略错误
file=codecs.open("D:\\朱烜宇\\day6\\kaifangX.txt","rb","gbk","ignore")
while True:
    mystr=input("请输入你要查找的信息")
    while True:
     linestr=file.readline()#读取一行
     if linestr.find(mystr)!=-1:
        print(linestr,end="")#显示数据
     if linestr==None:#读取失败返回值为None
        break