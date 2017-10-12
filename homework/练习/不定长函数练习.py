def add(num1,num2):
    return num1+num2


def newadd(*num):
    lastnum=0
    for data in num:
        lastnum=data+lastnum
        print(lastnum)
        
print(newadd(1))
print(newadd(1,2))
print(newadd(1,2,3))
print(newadd(1,2,3,4))