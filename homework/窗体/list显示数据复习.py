import tkinter
win=tkinter.Tk()
mylist=tkinter.Listbox(win,width=100)
mylist.pack()
for item in ["1","asdasd","dfjjfs","djfksj"]:
    mylist.insert(tkinter.END,item)
win.mainloop()