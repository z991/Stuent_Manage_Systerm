def merge(mylist1,mylist2):
    mylistall=[]
    i1=0
    i2=0
    while i1<len(mylist1) and i2<len(mylist2)>0:
        if mylist1[i1]<mylist2[i2]:
            mylistall.append(mylist1[i1])
            i1+=1
        elif mylist1[i1]>mylist2[i2]:
            mylistall.append(mylist2[i2])
            i2+=1
        else:
            mylistall.append(mylist2[i2])
            i1+=1
            i2+=1
    while i1<len(mylist1):
        mylistall.append(mylist1[i1])
        i1+=1
    while i2<len(mylist2):
        mylistall.append(mylist2[i2])
        i2+=1
    return mylistall

mylist1=[11,3,5,7,9,4]
mylist2=[8,4,2,6]
mylist1.sort()
mylist2.sort()
print(merge(mylist1,mylist2))

