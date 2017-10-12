import turtle
turtle.screensize(3024,2768)#屏幕
turtle.showturtle()

turtle.right(60)
turtle.circle(100,steps = 3)

turtle.left(60)

turtle.penup()
turtle.goto(200,0)
turtle.pendown()
turtle.right(45)
turtle.circle(100,steps=4)
turtle.left(45)


turtle.penup()
turtle.goto(400,0)
turtle.pendown()
turtle.right(36)
turtle.circle(100,steps=5)
turtle.left(36)

turtle.goto(600,0)
turtle.pendown()
turtle.right(60)
turtle.circle(100,steps=6)
turtle.left(60)



turtle.done()