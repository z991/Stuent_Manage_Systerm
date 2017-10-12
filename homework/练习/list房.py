import codecs
file=codecs.open("D:\\朱烜宇\\day6\\就业.txt","rb","gbk","ignore")
listname=file.readlines()
print(type(listname))
print(len(listname))
while True:
    name=input("请输入要查询的负心人")
    i=0
    for line in listname:
        if line.find(name)!=-1:
           i=i+1
           print(line)
