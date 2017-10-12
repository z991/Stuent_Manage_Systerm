import tkinter
import re

QQstr="""
this is QQ
"""
baklist=None



def  go():

    mylist=re.findall("[1-9]\\d{4,10}",text.get("0.0","end"))
    print(mylist)
    global baklist
    baklist=[]
    for  qq  in mylist:
        qq+="@qq.com"
        baklist.append(qq)
        list.insert(tkinter.END,qq)

    pass

def save():
    file =open(r"C:\Users\10499\Desktop\QQ邮箱银川酒吧.txt","wb")
    if  baklist!=None:
        for  QQ in baklist:
            file.write((QQ+"\r\n").encode("utf-8"))
    file.close()



win=tkinter.Tk()

button=tkinter.Button(win,text="提取",command=go)
button.pack()
button1=tkinter.Button(win,text="保存",command=save)
button1.pack()

text=tkinter.Text(win)
text.insert(tkinter.INSERT,QQstr)
text.pack()


list=tkinter.Listbox(win)
list.pack()

win.mainloop()

