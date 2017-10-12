x,y=eval(input("请输入一个点的坐标"))
import turtle
turtle.showturtle
turtle.penup()
turtle.goto(200,100)
turtle.pendown()
turtle.goto(200,-100)
turtle.goto(-200,-100)
turtle.goto(-200,100)
turtle.goto(200,100)

turtle.penup()
turtle.goto(x,y)
turtle.dot(10,"red")
turtle.pendown()

import math
x=abs(x)
y=abs(y)
if x<200 and y<100:
 print("在矩形内")
elif (x==200 and y<=100) or (x<=200 and y==100):
 print("在矩形上")
else:
 print("在矩形外")


turtle.done()