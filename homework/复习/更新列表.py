mylist=[1,2,3,4,5,6]
for  i  in range(len(mylist)): #修改列表必须索引
    if  mylist[i]==3:  #修改列表 ，mylist[i]是原本
        mylist[i]=9999
print(mylist)