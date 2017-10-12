import  win32com
import win32com.client
def makeexcel(name):
    print(name)
    #操作word,
    ex=win32com.client.Dispatch("Excel.Application")
    wk=ex.Workbooks.Add() #插入文档
    nowwk=wk.ActiveSheet
    ex.Visible=True #可见
    for i in range(1,10):
        nowwk.Cells(i,i).value=name+str(i)
    filename="C:\\Users\\Administrator\\Desktop\\"+name+".xls"
    wk.SaveAs(filename)
    wk.Close(True)
    ex.Application.Quit()


names=["李鑫","申羚锐","何丰城","孙雨"]
for name in names:
    makeexcel(name)

