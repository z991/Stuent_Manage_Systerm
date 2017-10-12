import re
import tkinter


phonestr="""
        请输入文本
    """
baklist=None
baklist1=None
def go():
    print(text.get("0.0","end"))
    mylist=re.findall("1[34578]\\d{9}",text.get("0.0","end"))
    print(mylist)
    for phone in mylist:
        list.insert(tkinter.END,phone)
        global baklist
        baklist=mylist
    pass

def yx():
    print(text.get("0.0", "end"))
    mylist1 = re.findall("[a-zA-Z0-9_.-]+@[a-zA-Z0-9_.-]+", text.get("0.0", "end"))
    print(mylist1)
    for mail in mylist1:
        list.insert(tkinter.END, mail)
        global baklist1
        baklist1 = mylist1
    pass

def savesj():
    file=open(r"F:\大数据\通讯录\提取后的数据\手机号\百度内部手机号.txt","wb")
    if baklist!=None:
        for qq in baklist:
            file.write((qq+"\r\n").encode("utf-8"))
    file.close()

    pass
def saveyx():
        file = open(r"F:\大数据\通讯录\提取后的数据\邮箱\百度内部邮箱.txt", "wb")
        if baklist1 != None:
            for mail in baklist1:
                file.write((mail + "\r\n").encode("utf-8"))
        file.close()







win=tkinter.Tk()
baklist=None


button=tkinter.Button(win,text="提取手机号",command=go)
button.pack()
button1=tkinter.Button(win,text="保存手机号",command=savesj)
button1.pack()
button2=tkinter.Button(win,text="保存邮箱",command=saveyx)
button2.pack()
button3=tkinter.Button(win,text="提取邮箱",command=yx)
button3.pack()

text=tkinter.Text(win)
text.insert(tkinter.INSERT,phonestr)
text.pack()

list=tkinter.Listbox(win)
list.pack()

win.mainloop()

