import codecs
filepath=r"D:\朱烜宇\大数据相关数据\dangdangwang.txt"
file=codecs.open(filepath,"rb","gbk","ignore")
for line in file:
    print(line)