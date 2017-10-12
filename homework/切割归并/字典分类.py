import codecs
import pickle
filepath=r"F:\大数据\Myspace.com\提取\Myspcelyx.txt"
file=codecs.open(filepath,"rb","utf-8","ignore")

mydicx={"123":file}
mylist=file.readlines()
file.close()
print("load")

mydict={"@gmail.com":"@gmail.com",
"@yahoo.com":"@yahoo.com",
"@yahoo.com.cn":"@yahoo.com.cn",
"@msn.com":"@msn.com",
"@hotmail.com":"@hotmail.com",
"@aol.com":"@aol.com",
"@ask.com":"@ask.com",
"@live.com":"@live.com",
"@qq.com":"@qq.com",
"@0355.net":"@0355.net",
"@163.com":"@163.com",
"@163.net":"@163.net",
"@263.net":"@263.net",
"@3721.net":"@3721.net",
"@yeah.net":"@yeah.net",
"@googlemail.com":"@googlemail.com",
"@mail.com":"@mail.com",
"@hotmail.com":"@hotmail.com",
"@msn.com":"@msn.com",
"@yahoo.com":"@yahoo.com",
"@gmail.com":"@gmail.com",
"@aim.com":"@aim.com",
"@aol.com":"@aol.com",
"@mail.com":"@mail.com",
"@walla.com":"@walla.com",
"@inbox.com":"@inbox.com",
"@126.com":"@126.com",
"@163.com":"@163.com",
"@sina.com":"@sina.com",
"@21cn.com":"@21cn.com",
"@sohu.com":"@sohu.com",
"@yahoo.com.cn":"@yahoo.com.cn	",
"@tom.com":"@tom.com",
"@qq.com":"@qq.com",
"@etang.com":"@etang.com",
"@eyou.com":"@eyou.com",
"@56.com":"@56.com",
"@x.cn":"@x.cn",
"@chinaren.com":"@chinaren.com",
"@sogou.com":"@sogou.com",
"@citiz.com":"@citiz.com",
"@hongkong.com":"@hongkong.com ",
"@ctimail.com":"@ctimail.com",
"@hknet.com ":"@hknet.com",
"@netvigator.com":"@netvigator.com",
"@mail.hk.com ":"@mail.hk.com ",
"@swe.com.hk":"@swe.com.hk",
"@ITCCOLP.COM.HK":"@ITCCOLP.COM.HK",
"@BIZNETVIGATOR.COM":"@BIZNETVIGATOR.COM",
"@aol.com ":"@aol.com",
"@netzero.net ":"@netzero.net",
"@twcny.rr.com":"@twcny.rr.com",
"@comcast.net":"@comcast.net",
"@warwick.net":"@warwick.net ",
"@verizon.net":"@verizon.net"
       }

filedict={}
for key in mydict:
    filepath="F:\大数据\Myspace.com\邮箱分类\\"+mydict[key]+".txt"
    fileo=open(filepath,"wb")
    filedict[mydict[key]]=fileo


print("create")


for line in mylist:

    chstr=mylist[0] #取出6个字符
    #mydict[chstr]  新疆维吾尔族自治区阿勒泰地区福海县
    if  chstr  in   mydict.keys():
        if  mydict[chstr]  in  filedict.keys():
            filedict[mydict[chstr]].write(line.encode("utf-8"))


print("over")
for key in filedict:
    filedict[key].close

