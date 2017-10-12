import tkinter
def go():
    pass
win=tkinter.Tk()
button=tkinter.Button(win,text="有种点我",command=go)
button.pack()
#entry1=tkinter.Entry(win,width=50,bg="red",fg="black")
entry1=tkinter.Entry(win,show="*",width=50,bg="red",fg="black")
entry1.pack()
win.mainloop()