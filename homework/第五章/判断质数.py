def isit(num):
    if num<0:
        return False
    elif num==0 or num==1:
        return False
    elif num==2 or num==3:
        return True
    else:
        isdata=True
        for i in range(2,num):
            if num%i==0:
                isdata=False
                break
        return isdata
print (isit(10))