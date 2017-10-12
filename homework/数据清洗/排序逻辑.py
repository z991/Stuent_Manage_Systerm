mylist=["a","a","b","c","c","c","d","d","d","d"]
length=len(mylist)

i=0
while i<length-1:
    times=1
    passwordstr=mylist[i]
    while i+1<=length-1 and mylist[i]==mylist[i+1]:
        times=times+1
        i=i+1

    print(times,passwordstr)
    i+=1
