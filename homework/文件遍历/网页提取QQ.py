import urllib.request #请求
import re

QQregex=re.compile(r"[1-9]\d{4,10}",re.IGNORECASE)

for  line  in urllib.request.urlopen("http://tieba.baidu.com/p/4803152690?pid=108523787272&cid=0#108523787272"):
    line=line.decode("utf-8")
    mylist = QQregex.findall(line)
    if mylist:
     print(mylist)
