import re
import tkinter


mailstr="""
        请输入文本
    """
baklist=None

def go():

    mylist=re.findall("[a-zA-Z0-9_.-]+@[a-zA-Z0-9_.-]+",text.get("0.0","end"))
    print(mylist)
    for mail in mylist:
        list.insert(tkinter.END,mail)
        global baklist
        baklist=mylist
    pass
def save():
    file=open(r"F:\大数据\通讯录\提取后的数据\邮箱.txt","wb")
    if baklist!=None:
        for mail in baklist:
            file.write((mail+"\r\n").encode("utf-8"))
    file.close()

    pass








win=tkinter.Tk()
baklist=None


button=tkinter.Button(win,text="提取",command=go)
button.pack()
button1=tkinter.Button(win,text="保存",command=save)
button1.pack()

text=tkinter.Text(win)
text.insert(tkinter.INSERT,mailstr)
text.pack()

list=tkinter.Listbox(win)
list.pack()

win.mainloop()