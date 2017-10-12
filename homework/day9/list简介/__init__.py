mylist=[1,2,3,4,5,6]
#mylist是一个多个变量组成的集合，每个变量
print(type(mylist))
print(id(mylist))
print(mylist)

mylist=[1,2,3,"ab",True]
print(id(mylist[0]))
mylist[0]=1000

print(type(mylist))
print(id(mylist))
print(mylist)