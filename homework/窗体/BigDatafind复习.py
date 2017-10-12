import codecs
import 窗体.ListShowdata复习
class bigdatafind:
    def __init__(self,path):
        self.file=codecs.open(path,"rb","GBK","ignore")#打开文件
        self.showdata=窗体.ListShowdata复习.showdatainlist()
        pass
    def find(self,searchstr):
        while  True:
            line=self.file.readline()
            if line.find(searchstr)!=-1:
                print(line,end="") #显示数据
                self.showdata.adddata(line) #插入
            if  not line: #读不到数据退出
                break
        pass
    def show(self):
        self.showdata.show()
        pass
    def  __del__(self):
        self.file.close()