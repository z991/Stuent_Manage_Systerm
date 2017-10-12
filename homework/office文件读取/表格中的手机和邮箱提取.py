import codecs
import re
filepath=r"D:\朱烜宇\day24down\xlsx1111.txt"
file=open(filepath,"r")
mylist=re.findall("[a-zA-Z0-9_.-]+@[a-zA-Z0-9_.-]+",)
#mylist=re.findall(file.read(("[a-zA-Z0-9_.-]+@[a-zA-Z0-9_.-]+")))
print(mylist)
'''file=open(r"D:\朱烜宇\day24down\111.txt","wb")
if mylist!=None:
    for mail in mylist:
        file.write((mail+"\r\n").encode("utf-8"))
    file.close()'''
