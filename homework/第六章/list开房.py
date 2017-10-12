#字符串检索，
#print("hello".find("el")) #find函数找到返回位置
#print("hello".find("ak"))

import codecs  #编码
#第一个参数路径，第二个参数，rb二进制读写 第三个参数汉字编码，第十四个参数忽略错误
file=codecs.open("D:\\朱烜宇\\day6\\就业.txt","rb","gbk","ignore")
listname=file.readlines()
print(type(listname))
print(len(listname))
while True:
    name=input("输入要查询的负心人")
    i=0
    for line in listname:
        if line.find(name)!=-1:
            i=i+1
            print(line)
    print("一共"+str(i)+"条")