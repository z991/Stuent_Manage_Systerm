mylist=["122",2.6,3,4,5,6,7]
print(id(mylist))
for i in range(len(mylist)):
    print(mylist[i],id(mylist[i]))#每个元素都有一个地址，元素是变量，元素的地址是不变的