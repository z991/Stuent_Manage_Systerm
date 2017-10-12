import tkinter
from  tkinter import ttk  #导入内部包
class  Tableshowdata:
    def  __init__(self):
        self.win=tkinter.Tk() #构造窗体
        self.win.geometry("900x800+0+0")
        self.tree = ttk.Treeview(self.win,height=800)  # 表格
        self.idnum=0 #插入的位置
        self.tree["columns"] = ("user", "password", "email")
        self.tree.column("user", width=200)  # 表示列,不显示
        self.tree.column("password", width=200)
        self.tree.column("email", width=200)

        self.tree.heading("user", text="CSDN-name")  # 显示表头
        self.tree.heading("password", text="CSDN-age")
        self.tree.heading("email", text="CSDN-tall")


    def addata(self,insertstr): #增加数据
        datalist=insertstr.split(" # ")
        if len(datalist)==3:
            self.tree.insert("", self.idnum, text="line"+str(self.idnum+1), values=(datalist[0], datalist[1], datalist[2]))  # 插入的行数，
            self.idnum+=1
    def  show(self):
        self.tree.pack()
        self.win.mainloop()  # 进入消息循环

'''  作为执行代码，import 执行代码都会执行
mylist=Tableshowdata()
mylist.addata("19810831 # 273018 # wangweirun@sina.com")
mylist.addata("19811103 # 74215 # luckyydd@263.net")
mylist.addata("198212160123 # 433318 # xpj-1216@163 com")
mylist.show()
'''


