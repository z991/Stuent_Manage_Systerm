import tkinter
import os
def go():
    os.system("calc")
win=tkinter.Tk()
win.title("hello libai")
win.geometry("800x800+300+0")
button=tkinter.Button(win,text="有种点我",command=go)
button.pack()
button1=tkinter.Button(win,text="有种点",command=lambda:print("hellow world"),width=100,height=200)
button1.pack()
win.mainloop()