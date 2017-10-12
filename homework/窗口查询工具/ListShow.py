import tkinter
class  Listshowdata:
    def  __init__(self):
        self.win=tkinter.Tk() #构造窗体
        self.win.geometry("900x800+0+0")
        self.mylist=tkinter.Listbox(self.win,width=900,height=800) #列表框
        self.mylist.pack()
    def addata(self,insertstr): #增加数据
        self.mylist.insert(tkinter.END,insertstr)
    def  show(self):
        self.win.mainloop()  # 进入消息循环

'''
mylist=Listshowdata()
mylist.addata("sadsadsadsa")
mylist.addata("sadsadsadsa")
mylist.addata("sadsadsadsa")
mylist.show()
'''