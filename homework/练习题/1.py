num=eval(input("请输入一个20以内的数"))
if num==0:
    print("sum=0")
elif num<20:
    sum = 1
    for i in range(1, num + 1):
        sum = i * sum
    print(sum)
else:
    print("输入错误，请重新输入")