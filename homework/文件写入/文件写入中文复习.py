file=open(r"C:\Users\Tsinghua-yincheng\Desktop\day11\newchina1.txt","wb") #写入二进制
mystr="""
一位python程序员的七夕情书
"""
#python默认编码是UTF-8
print(type(mystr.encode("utf-8")))
file.write(mystr.encode("utf-8")) #write,只能写入二进制
file.close()