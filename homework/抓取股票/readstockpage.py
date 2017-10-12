import urllib
import urllib.request

def  getpage(path):
    data=urllib.request.urlopen(path).read().decode("gbk") #中文网页
    return data

path="http://quote.eastmoney.com/stocklist.html"
print(getpage(path))
