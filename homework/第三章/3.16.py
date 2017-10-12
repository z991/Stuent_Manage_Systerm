import turtle
turtle.showturtle

turtle.screensize(3024,2768)#屏幕
turtle.right(60)
turtle.begin_fill()
turtle.circle(100,steps=3)
turtle.color("blue")
turtle.end_fill()
turtle.left(60)

turtle.penup()
turtle.goto(200,0)
turtle.pendown()
turtle.right(45)
turtle.begin_fill()
turtle.circle(100,steps=4)
turtle.color("black")
turtle.end_fill()
turtle.left(45)

turtle.penup()
turtle.goto(400,0)
turtle.pendown()
turtle.right(36)
turtle.begin_fill()
turtle.circle(100,steps=5)
turtle.color("white")
turtle.end_fill()
turtle.left(36)

turtle.penup()
turtle.goto(600,0)
turtle.pendown()
turtle.right(30)
turtle.begin_fill()
turtle.circle(100,steps=6)
turtle.color("yellow")
turtle.end_fill()
turtle.left(30)


turtle.penup()
turtle.goto(900,0)
turtle.pendown()
turtle.right(22.5)
turtle.begin_fill()
turtle.circle(100,steps=8)
turtle.color("pink")
turtle.end_fill()
turtle.left(22.5)

turtle.done()