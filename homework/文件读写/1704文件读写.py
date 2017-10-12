'''
1.打开文件
open(path,flag)
path:要打开文件的路径
flag:打开方式
r: 以只读的方式打开此文件，文件的描述符放在文件的开头
rb:以二进制格式打开一个文件用于只读，文件的描述符放在文件的开头

r+:打开一个文件用于读写,文件的描述符放在文件的开头

w:打开一个文件用于写入，如果文件存在会覆盖，如果不存在会创建新的文件

wb:打开一个文件只用于写入二进制，如果文件存在会覆盖，如果不存在会创建新的文件

w+:打开一个文件用于读写，如果文件存在会覆盖，如果不存在会创建新的文件

a:打开一个文件用于追加，如果文件存在，文件描述符将会放到文件末尾

a+:

encoding:编码格式
errors:错误处理
'''
path=r"H:\1704\day07\5-文件读写\file1.txt"
# f=open(path,"r",encoding="utf-8",errors="ignore")
#
# '''
# 2.读取文件
# '''
# #1.读取文件全部内容
# # str1=f.read()
# # print(str1)




#关闭文件
# f.close()

with open(path,"r",encoding="utf-8") as f:
    print(f.read())