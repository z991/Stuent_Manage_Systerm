mylist=dir("")#dir返回的是一个list
'''print(type(""))
print(mylist)

for i in mylist:
    print(i)
    print(help("str."+i))'''

for i in range(len(mylist)):
    print(mylist[i])
    print(help("str."+mylist[i]))