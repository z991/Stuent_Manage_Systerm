import turtle


#设定循环次数
#实现一个操作，常量
#常量修改变量

length=50 #初始
step=50  #每次加50
num=0   #循环10次，
for i in range(0,10,50):
while num<10:
    print(num)
    num+=1  #循环次数


    turtle.penup()
    turtle.goto(length, length)
    turtle.pendown()
    turtle.goto(length, -1 * length)
    turtle.goto(-1 * length, -1 * length)
    turtle.goto(-1 * length, length)
    turtle.goto(length, length)
    length+=step

else:
    print("out",num)
turtle.done()
