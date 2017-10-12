import tkinter
import  窗体.BigDatafind复习


class InputView:
    def __init__(self):
        self.win=tkinter.Tk()
        from  tkinter import ttk
        self.win.geometry("400x400+300+0")  # 800宽度，800高度，x,y坐标，左上角
        comvalue = tkinter.StringVar()  # 窗体自带的文本，新建一个值
        comboxlist = ttk.Combobox(self.win, textvariable=comvalue)  # 初始化
        comboxlist["values"] = ("1", "2", "3", "4")
        comboxlist.current(0)  # 选择第一个

        comboxlist.pack()
        self.entry = tkinter.Entry(self.win)  # input
        self.entry.place(x=100, y=400)

        self.button1 = tkinter.Button(self.win, text="搜索结果且list显示",command=self.search)  # 收到消息执行这个函数
        self.button1.place(x=100,y=50)
        self.button2 = tkinter.Button(self.win, text="搜索结果且table显示", )  # 收到消息执行这个函数
        self.button2.place(x=100, y=100)
        pass
    def show(self):
        self.win.mainloop()
        pass
    def search(self):
        print("start search",self.entry.get())
        bigfind = 窗体.BigDatafind复习.bigdatafind(r"D:\朱烜宇\大数据相关数据\nasa.txt")
        bigfind.find(self.entry.get())
        bigfind.show()
        pass

