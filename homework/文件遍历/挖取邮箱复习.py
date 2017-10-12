import urllib
import urllib.request #请求
import re

mailregex=re.compile(r"([A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4})",re.IGNORECASE)

'''
for  line  in urllib.request.urlopen("http://bbs.tianya.cn/m/post-140-393974-6.shtml"):
    mylist=mailregex.findall(line.decode("utf-8"))
    if  mylist:
        print(mylist)
'''
mystr=urllib.request.urlopen("http://tieba.baidu.com/p/5118638503").read()
mylist=mailregex.findall(mystr.decode("utf-8"))
print(mylist)
file =open(r"F:\DAY\day19down\云计算邮箱保存1.txt","wb")
for  mail in mylist:
    file.write((mail+"\r\n").encode("utf-8"))
file.close()