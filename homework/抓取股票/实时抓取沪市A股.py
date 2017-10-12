import urllib
import urllib.request
import re
#抓取网页源代码
def getpage(path):
    data=urllib.request.urlopen(path).read().decode("gbk")
    return data
#生成网页列表
def runpage(min,max):
    for page in range(min,max):
        mystr="http://quote.stockstar.com/stock/sha_3_1_"+str(page)+".html"
        print(mystr)

def gettbody(data):
    pat=re.compile("<tbody>[\s\S]*</tbody>")
    body=pat.findall(data)

    patnew=re.compile(">(.*?)<")
    datalist=patnew.findall(body[0])
    return datalist
def showdata(datalist):
    newdatalist=datalist.copy()
    for data in datalist:
        if data=="":
            newdatalist.remove(data)
    mynidex=-1
    for i in range(len(newdatalist)):
        newdatalist[i].strip()
        if newdatalist[i]=="603938":
            myindex=i
    print("myindex",myindex)
    for i in range(myindex,len(newdatalist),12):
            for j in range (12):
                if i+j<len(newdatalist):
                    print(format(newdatalist[i+j],"<15s"),end=" ")
            print("")
data =getpage("http://quote.stockstar.com/stock/sha_3_1_1.html")
print(showdata(gettbody(data)))


