def merge(mylist1,mylist2):
    mylistall=[]
    while len(mylist1)>0 and len(mylist2)>0:
        if mylist1[0]<mylist2[0]:
            mylistall.append(mylist1[0])
            del mylist1[0]
        else:
            mylistall.append(mylist2[0])
            del mylist2[0]
    mylistall.extend(mylist1)
    mylistall.extend(mylist2)
    return mylistall
mylist1=[11,3,5,7,9]
mylist2=[8,4,2,6]
mylist1.sort()
mylist2.sort()
print(merge(mylist1,mylist2))


