'''#读取英文
file=open(r"D:\朱烜宇\day11\1.txt","r")
mystr=file.read()
print(mystr)
file.close'''

#读取中文
file=open(r"D:\朱烜宇\day11\newchina.txt","rb")
mystr=file.read()
print(mystr.decode("utf-8"))