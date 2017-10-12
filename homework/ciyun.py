#coding:utf8
import urllib2,re
first_url="http://www.jianshu.com/"
response=urllib2.urlopen(first_url)
html=response.read()
# print (html)
content_url=re.findall(r'<ul class="note-list" infinite-scroll-url="/">(.*？)</ul>', html, re.S)
#print (content_url)
a_list = re.findall(r'<a class="title" target="_blank".*?</a>', content_url)
href_list=[]
for a in a_list:
    href=re.findall(r'href="(.*?)"',a)
    href="%s%s" % (first_url,href)
    href_list.append(href)
print(href_list)