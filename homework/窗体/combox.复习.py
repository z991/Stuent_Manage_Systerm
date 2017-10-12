import tkinter
from  tkinter  import ttk
def go(*args): #处理事件
    print(comboxlist.get()) #选中当前的值



win=tkinter.Tk() #构造窗体
comvalue=tkinter.StringVar()#窗体自带的文本，新建一个值
comboxlist=ttk.Combobox(win,textvariable=comvalue) #初始化
comboxlist["values"]=("1","2","3","4")
comboxlist.current(0)#选择第一个
comboxlist.bind("<<ComboboxSelected>>",go) #绑定事件
comboxlist.pack()



win.mainloop() #进入消息循环