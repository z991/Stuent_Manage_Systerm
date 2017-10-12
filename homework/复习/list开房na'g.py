import codecs
file=codecs.open("D:\\朱烜宇\\day6\\就业.txt","rb","gbk","ignore",)
listname=file.readlines()
while True:
    name=input("请输入数据")
    i=0
    for line in listname:
        if line.find(name)!=-1:
            i+=1
            print(line)
    print("一共"+str(i)+"条")