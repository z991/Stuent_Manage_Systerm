import tkinter
class  Textshowdata:
    def  __init__(self):
        self.win=tkinter.Tk() #构造窗体
        self.win.geometry("900x800+0+0")
        self.text = tkinter.Text(self.win,width=900,height=800)  # 文本编辑器
        self.text.pack()
    def addata(self,insertstr): #增加数据
        self.text.insert(tkinter.INSERT, insertstr)
    def  show(self):
        self.win.mainloop()  # 进入消息循环

'''
mylist=Textshowdata()
mylist.addata("sadsadsadsa\r\n")
mylist.addata("sadsadsadsa\r\n")
mylist.addata("sadsadsadsa")
mylist.show()

'''
