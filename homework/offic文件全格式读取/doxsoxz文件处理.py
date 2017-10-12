import win32com
import docx
import win32com.client
myword=win32com.client.Dispatch("Word.Application") #调用系统word功能
path=r"H:\DAY\day24down\doc\Python正则表达式七种兵器.docx" #处理doc,docx
doc=myword.Documents.Open(path)#打开
doc.SaveAs(r"H:\DAY\day24down\doc\211.txt",2) #编号为2保存为txt ,save必须绝对路径
doc.Close() #关闭
myword.Quit() #退出'''