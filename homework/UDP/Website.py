import urllib.request
try:
    data=urllib.request.urlopen("http://www.qinghuabeida.cn/Webadmin").read()
    print(data)
    print("页面存在")
except:
    print("页面不存在")