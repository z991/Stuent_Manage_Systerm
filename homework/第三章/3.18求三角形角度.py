import math
x1,y1,x2,y2,x3,y3=eval(input("Enter three points: "))
a=math.sqrt((x2-x3)*(x2-x3)+(y2-y3)*(y2-y3))
b=math.sqrt((x1-x3)*(x1-x3)+(y1-y3)*(y1-y3))
c=math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))

A=math.degrees(math.acos((a*a-b*b-c*c)/(-2*b*c)))
B=math.degrees(math.acos((b*b-a*a-c*c)/(-2*a*c)))
C=math.degrees(math.acos((c*c-a*a-b*b)/(-2*a*b)))
print("The three angles are ",round(A*100)/100.0,
      round(B* 100) / 100.0,
round(C*100)/100.0)
import turtle
turtle.showturtle
turtle.penup()
turtle.goto(x1,y1)
turtle.down()
turtle.write(round(A,2))

turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.goto(x2,y2)
turtle.write(round(B,2))

turtle.penup()
turtle.goto(x2,y2)
turtle.pendown()
turtle.goto(x3,y3)
turtle.write(round(C,2))

turtle.penup()
turtle.goto(x3,y3)
turtle.pendown()
turtle.goto(x1,y1)

turtle.done()

