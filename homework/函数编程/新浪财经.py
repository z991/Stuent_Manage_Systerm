import urllib
import urllib.request

for i in range(100,150):
    url="http://hq.sinajs.cn/list=sz300"+str(i)
    print(urllib.request.urlopen(url).read().decode("gbk"))