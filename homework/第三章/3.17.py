import math
x1,y1,x2,y2,x3,y3=eval(input("请输入三角形三个定点的坐标p1,p2,p3: "))
a=math.sqrt((x2-x3)*(x2-x3)+(y2-y3)*(y2-y3))
b=math.sqrt((x1-x3)*(x1-x3)+(y1-y3)*(y1-y3))
c=math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
print(a,b,c)
s=(a+b+c)/2
print(s)
area=(s*(s-a)*(s-b)*(s-c))**0.5
print(area)

import turtle
turtle.showturtle

turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.write("c"+str(x1)+","+str(y1)+")")
turtle.up()
turtle.goto(x1,y1)
turtle.pendown()
turtle.goto(x2,y2)

turtle.write("c"+str(x2)+","+str(y2)+")")
turtle.up()
turtle.goto(x2,y2)
turtle.pendown()
turtle.goto(x3,y3)

turtle.write("c"+str(x3)+","+str(y3)+")")
turtle.up()
turtle.goto(x3,y3)
turtle.pendown()
turtle.goto(x1,y1)
turtle.hideturtle()
turtle.penup()

x=min(x1,x2,x3)
y=(min(y1,y2,y3))-40
turtle.goto(x,y)
turtle.pendown()
turtle.write("the area of the triangle is:",area)

turtle.done()