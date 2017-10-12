"""number=eval(input("请输入一个数:"))
if number %2  ==0:
    print(number,"是偶数")
else:
    print(number,"是奇数")"""
import random
number1=random.randint(0,9)
number2=random.randint(0,9)
if number1<=number2:
    number1,number2=number2,number1
answer=eval(input("what is"+str(number1)+"-"+str(number2)+"?"))
if number1-number2==answer:
    print("You are corrcect!")
else:
    print("Your answer is  wrong.\n",number1,"-",number2,"is",number1-number2,".")
