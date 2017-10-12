import tkinter
class  showdatainlist:
    def __init__(self):
        self.win = tkinter.Tk()
        self.win.geometry("900x800+0+0")
        self.list=tkinter.Listbox(self.win,width=900,height=800) #list
        self.list.pack() #加载到窗体
    def show(self):
        self.win.mainloop()
    def adddata(self,insertstr):
        self.list.insert(tkinter.END,insertstr)#插入数据
        pass