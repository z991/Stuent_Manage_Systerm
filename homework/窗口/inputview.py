import tkinter

class InputView:
    def __init__(self):
        self.win=tkinter.Tk()
        self.win.geometry("400x400+300+0")



        self.entry = tkinter.Entry(self.win)  # input
        self.entry.place(x=0, y=0)

        self.button1 = tkinter.Button(self.win, text="搜索结果且list显示", command=self.search)  # 收到消息执行这个函数
        self.button1.place(x=100, y=50)





        pass
    def show(self):
        self.win.mainloop()
        pass
    def search(self):
        pass