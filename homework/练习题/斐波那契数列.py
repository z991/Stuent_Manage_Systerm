
# if N==1:
#     j=0
# elif N==2:
#     j=1
# else:
#     j=1
#     for i in  range(0,N):
#         j=
def item( num ):
    if num == 0 :
        res = 0
    elif num == 1:
        res = 1
    else:
        res = item ( num - 1) + item (num -2)
    return res
def printFibo(no):
    i = 0
    while i < no-1:
        i += 1
    print(item(i))
printFibo(10)