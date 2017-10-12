#画几乘几的   方格


steps=eval(input("请输入方格的边长"))
x,y=eval(input("请输入横竖的格数"))

def FG():
    import turtle
    turtle.showturtle()
    step =steps
    for i in range(x+1):  # 0-18
        turtle.penup()
        turtle.goto(0, steps * i)
        turtle.pendown()
        turtle.forward(steps* x)

    turtle.right(270)
    for i in range(y+1):  # 0-18
        turtle.penup()
        turtle.goto(steps * i, 0)
        turtle.pendown()
        turtle.forward(steps * y)


    turtle.done()
print (FG())