import threading
import codecs
import os
class MyThreadLine(threading.Thread):#定义一个统计行数的类
    def __init__(self,path):
        threading.Thread.__init__(self)#父类初始化
        self.path=path#路径
        self.line=-1#行数
    def run(self):
        file = codecs.open(self.path, "rb", "gbk", "ignore")
        listname = file.readlines()
        lines=0
        for item in listname:
            lines+=1
        self.line=lines
path=r"F:\大数据\邮箱\163mail2\163邮箱2-06.txt"
mythd=MyThreadLine(path)
mythd.start()
mythd.join()
print(mythd.line)