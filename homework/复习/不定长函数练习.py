def add(num1,num2):
    return num1+num2
def newadd(*num):
    lastnum=0
    for data in num:
        lastnum+=data
    print(lastnum)

newadd(1,2,3)
newadd(1,2,5,8,9)