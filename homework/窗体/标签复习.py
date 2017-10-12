import tkinter
win=tkinter.Tk()
win.geometry("500x500+300+0")
label=tkinter.Label(win,text="hello python")
label.pack()
newlabel=tkinter.Label(win,
                       anchor=tkinter.N,
                       bg="blue",
                        fg="yellow",
                       text="gogogo",
                       width=100,
                       height=50)
newlabel.pack()
win.mainloop()