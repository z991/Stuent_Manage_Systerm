import codecs #编码解码
import 窗口查询工具.ListShow
import  窗口查询工具.TableShow
import  窗口查询工具.TextShow
class bigdatafind:
    def __init__(self,path,howtoshow):
        self.file=codecs.open(path,"rb","GBK","ignore")#打开文件
        self.howtoshow=howtoshow
        self.showview=None  #窗体-创建
        if  self.howtoshow=="listshow":
            self.showview=窗口查询工具.ListShow.Listshowdata()
        elif  self.howtoshow=="textshow":
            self.showview = 窗口查询工具.TextShow.Textshowdata()
        else:
            self.showview=窗口查询工具.TableShow.Tableshowdata()


    def find(self,searchstr):
        while  True:
            line=self.file.readline()
            if line.find(searchstr)!=-1:
                print(line,end="") #显示数据
                #插入
                if self.showview != None:
                    self.showview.addata(line)  # 显示

            if  not line: #读不到数据退出
                break
    def show(self):
        if  self.showview!=None:
            self.showview.show() #显示
    def  __del__(self):
        self.file.close()


'''
#print("hello world")
big=bigdatafind("Z:\\F\\第一阶段视频\\20170424\\data\\csdnindexsort.txt","listshow")
big.find("yincheng")
big.show()
'''
