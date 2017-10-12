import turtle
turtle.showturtle
R=eval(input("五环的半径: "))
turtle.pensize(20)
turtle.goto(0,0)
turtle.color("blue")
turtle.circle(R)

turtle.penup()
turtle.goto(R*2,0)
turtle.pendown()
turtle.color("yellow")
turtle.circle(100)

turtle.penup()
turtle.goto(R*4,0)
turtle.pendown()
turtle.color("black")
turtle.circle(100)

turtle.penup()
turtle.goto(R,-R)
turtle.pendown()
turtle.color("green")
turtle.circle(R)

turtle.penup()
turtle.goto(3*R,-R)
turtle.pendown()
turtle.color("red")
turtle.circle(R)

'''turtle.penup()
turtle.goto(250,-200)
turtle.pendown()
turtle.write("奥运五环",font=("华文琥珀",20,"normal"))'''




turtle.done()