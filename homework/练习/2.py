import random
number1=random.randint(0,13)
number2=random.randint(0,13)

print("小宝宝 %d+%d"%(number1,number2))
num=input("baby input")
num=eval(num)
if num==number1+number2:
    print("小宝宝你真棒")