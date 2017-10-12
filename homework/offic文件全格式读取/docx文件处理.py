import docx  #只能处理docx文件
def  getText(filepath):
    doc=docx.Document(filepath)#打开文档
    fulltext=[]
    for  para in doc.paragraphs: #遍历每一个段落
        fulltext.append(para.text)
    return fulltext

data=getText(r"H:\DAY\day24down\doc\Python正则表达式七种兵器.docx")
for line in data:
    print(line)
