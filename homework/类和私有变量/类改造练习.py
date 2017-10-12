import tkinter
class  mywin:
    def  __init__(self,text,height,width,x,y):
        self.mytk=tkinter.Tk()
        self.mytk.title(text)
        self.height=height
        self.width=width
        self.x=x
        self.y=y
        laststr = "%dx%d+%d+%d" % (self.height, self.width, self.x, self.y)
        self.mytk.geometry(laststr)
    def show(self):
        self.mytk.mainloop()

win1=mywin("hello python1",300,400,0,0)
win1.show()
win2=mywin("hello python2",300,400,0,0)
win2.show()
win3=mywin("hello python3",300,400,0,0)
win3.show()