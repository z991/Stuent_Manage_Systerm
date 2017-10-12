import math
s=eval(input("请输入一个四位整数:"))
a=s//1000
b=(s-a*1000)//100
c=(s-a*1000-b*100)//10
d=s%10
print(str(d)+str(c)+str(b)+str(a))