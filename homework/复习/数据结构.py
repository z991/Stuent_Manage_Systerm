'''mylist=[1,2,3,4,5,6,7]
print(len(mylist))#列表，容纳多个数据
mylist.append(8)#增加数据
print(len(mylist))
for data in mylist:#循环遍历列表
    print("------",data)
print(mylist)
print(mylist[1:7])
print(mylist[4:-1])
print(mylist[:])'''
list=[1,2,3]
list[1]=10
print(list)
for i in range(len(list)):#索引循环
    print(list[i])