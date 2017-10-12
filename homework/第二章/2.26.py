x1,y2,radius=eval(input("Enter the center and the radius:"))
area=radius*radius*3.14
print(area)

import turtle
turtle.showturtle()
turtle.goto(x1,y2)
turtle.write(area)
turtle.penup()
turtle.right(90)
turtle.forward(radius)
turtle.pendown()
turtle.left(90)
turtle.circle(radius)
turtle.done()