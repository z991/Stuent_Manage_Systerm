import urllib
import urllib.request
import re
import os

def getpage(path):
    data=urllib.request.urlopen(path).read().decode("gbk")
    return data

def getcode(data):
    regex_str = " <li><a target=\"_blank\" href=\"http://quote.eastmoney.com/(\S\S.*?).html\">(.*?)\("
    pat = re.compile(regex_str)
    codelist=pat.findall(data)
    return codelist
def downloadstock(code,name,date):
    path="F:\\DAY\\抓取股票\\down"+date
    if not os.path.exists(path):
        os.makedirs(path)
    inshorsz=10
    if code[0:2]=="sh":
        inshorsz=0
    else:
        inshorsz=0
    if inshorsz!=10:
        url="http://quotes.money.163.com/service/chddata.html?code="+str(inshorsz)+code[2:]+"&end=20130523&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"
        path = "F:\\DAY\\抓取股票\\down" + date + "\\" + name + ".csv"
        urllib.request.urlretrieve(url,path)
path="http://quote.eastmoney.com/stocklist.html"
data=getpage(path)
codelist=getcode(data)
for code in codelist:
    try:
        downloadstock(code[0],code[1],"20170323")
    except:
        print("error")
