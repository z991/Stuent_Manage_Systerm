num=eval(input("请输入0-20之间的整数："))
if   num==0:
    print("0")
elif  num>20:
    print("输入有误")
else:
    sum=1
    for  i   in  range(1,num+1):
        sum*=i
        i+=1
    print(sum)
