import tkinter
import tkinter.ttk
import os
class TreeWindows:
    def __init__(self):
        self.win=tkinter.Tk()
        self.tree=tkinter.ttk.Treeview(self.win,height=500)
        self.ysb=tkinter.ttk.Scrollbar(self.win,orient="vertical",command=self.tree.yview())
        self.xsb = tkinter.ttk.Scrollbar(self.win, orient="horizontal",command=self.tree.xview())
        self.tree.configure(yscroll=self.ysb.set,xscroll=self.xsb.set)
        self.tree.grid(row=0,column=0)
        self.tree.heading("#0",text="Path",anchor="w")
        filepath="F:\\大数据\\通讯录"
        root=self.tree.insert("","end",text=filepath,open=True)
        self.loadtree(root,filepath)

        self.ysb.grid(row=0,column=1)
        self.xsb.grid(row=1,column=0)
        self.win.grid()

    def loadtree(self,parent,rootpath):
        for path in os.listdir(rootpath):
            abspath=os.path.join(rootpath,path)
            oid=self.tree.insert(parent,'end',text=path,open=False)

            if os.path.isdir(abspath):
                print("文件夹",abspath)
                self.loadtree(oid,abspath)
            else:
                print("文件",abspath)






    def show(self):
        self.win.mainloop()

mytree=TreeWindows()
mytree.show()