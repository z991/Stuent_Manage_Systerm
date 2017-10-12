import urllib
import urllib.request #请求
import re
import tkinter


mailstr="""
        请输入网址
    """
baklist=None

def  go():
    mailregex = re.compile(r"([A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4})", re.IGNORECASE)
    mystr = urllib.request.urlopen("unknown url type: 'mailstr'").read()
    mylist = mailregex.findall(mystr.decode("utf-8"))
    print(mylist)
    global baklist
    baklist=[]
    for  mail  in mylist:
        baklist.append(mail)
        list.insert(tkinter.END,mail)

def save():
    file = open(r"F:\DAY\day19down\邮箱保存2.txt", "wb")
    for mail in baklist:
        file.write((mail + "\r\n").encode("utf-8"))
    file.close()


    pass








win=tkinter.Tk()
baklist=None


button=tkinter.Button(win,text="挖取",command=go)
button.pack()
button1=tkinter.Button(win,text="保存",command=save)
button1.pack()

text=tkinter.Text(win)
text.insert(tkinter.INSERT,mailstr)
text.pack()

list=tkinter.Listbox(win)
list.pack()

win.mainloop()