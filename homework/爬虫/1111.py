#coding=utf-8
import time
import requests
from bs4 import BeautifulSoup
import os
import sys

if(os.name == 'nt'):
        print(u'你正在使用win平台')
else:
        print(u'你正在使用linux平台')

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
#http请求头
all_url = 'http://www.mzitu.com'
start_html = requests.get(all_url,headers = header)

#保存地址
path = 'D:/mzitu/'

#找寻最大页数
soup = BeautifulSoup(start_html.text,"html.parser")    #定义为beautifulsoup类parser
page = soup.find_all('a',class_='page-numbers') #page为一个列表，找到标签为a的，属性class为‘page-numbers'的标签
max_page = page[-2].text #观察最大页数在-2处，用.text取文本信息


same_url = 'http://www.mzitu.com/page/'
for n in range(1,int(max_page)+1):
    ul = same_url+str(n)
    start_html = requests.get(ul, headers=header)
    soup = BeautifulSoup(start_html.text,"html.parser")#标签的寻找find是一对一对的然后用text取其中内容
    all_a = soup.find('div',class_='postlist').find_all('a',target='_blank')#在find  div的大类下找到所有标签a且a标签中target为blank的标签(因为有多个a类标签，需要把没用的排除掉)
    for a in all_a:    #all_a一共找到两个部分，第一个部分是空的，第二部分才能提取得到title
        title = a.text #提取文本内容就是在<>尖括号以外的信息
        if(title != ''):
            print("准备扒取："+title)

            #win不能创建带？的目录  如果目录中含有?将其替换为''
            if(os.path.exists(path+title.strip().replace('?',''))):#如果目录存在(exist)返回1，flag = 1
                flag=1
            else:
                os.makedirs(path+title.strip().replace('?',''))
                flag=0
            os.chdir(path + title.strip().replace('?',''))#改变当前工作目录到指定路径
            href = a['href']#图片地址
            html = requests.get(href,headers = header)
            mess = BeautifulSoup(html.text,"html.parser")
            pic_max = mess.find_all('span')
            pic_max = pic_max[10].text #最大页数
            if(flag == 1 and len(os.listdir(path+title.strip().replace('?',''))) >= int(pic_max)):
                print('已经保存完毕，跳过')
                continue
            for num in range(1,int(pic_max)+1):
                time.sleep(1)#抓慢一点，上次爬的太快ip被封了
                pic = href+'/'+str(num)#图片所在页的地址
                html = requests.get(pic,headers = header)
                mess = BeautifulSoup(html.text,"html.parser")
                pic_url = mess.find('img',alt = title)#找到标签为img
                html = requests.get(pic_url['src'],headers = header)#这里找到的才是真正图片的地址
                file_name = pic_url['src'].split(r'/')[-1]#文件名为地址分割后的最后一个字符串
                f = open(file_name,'wb')
                f.write(html.content)#content是类函数，在这里就是地址html所表示的图片
                f.close()
            print('完成')
    print('第',n,'页完成')