num=eval(input("请输入数据数量"))
maxdata=eval(input("data"))
nextdata=eval(input("data"))
if maxdata<nextdata:
   temp=maxdata
   maxdata=nextdata
   nextdata=temp
for i in range(num-2):
    x=eval(input("data"))
    if x > maxdata:
        nexdata = maxdata
        maxdata = x
    elif x < maxdata:
        if x < nextdata:
            pass
        elif x > nextdata:
            nextdata = x
print("maxdata",maxdata)
print("nextdata",nextdata)