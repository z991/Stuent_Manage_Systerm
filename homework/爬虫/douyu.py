#coding=utf-8
#爬取斗鱼颜值妹子图片
import re
import urllib.request
import time
from bs4 import BeautifulSoup

#定义为方法
def getHTML(url):
    page = urllib.request.urlopen(url)
    html=page.read()
    return html

#开始根据链接爬图片保存数据
def getImage(html):
    #创建对象,传入网页数据
    soup1 = BeautifulSoup(html)
    soupL = soup1.select('#live-list-contentbox')
    print(str(soupL))
    strone = str(soupL)
    soup2 = BeautifulSoup(strone)
    soupLi = soup2.select('li')
    for soupLione in soupLi:
            #获取单个li标签获取数据
           soupone = BeautifulSoup(str(soupLione))
           name = soupone.a['title']
           print('开始下载:%s'%name)
           url = soupone.img['data-original']
           try:
               urllib.request.urlretrieve(url,'C:\\Users\\JackChiang\\Pictures\\PythonData\\%s.jpg'%name)
               print(url)
           except OSError:
               print('出现异常,地址为：%s'%url)
           finally:
               time.sleep(0.5)

fileimg = getHTML('https://www.douyu.com/directory/game/yz')
getImage(fileimg)
