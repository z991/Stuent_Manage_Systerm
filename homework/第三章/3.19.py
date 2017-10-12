import turtle
turtle.showturtle
x1,y1=eval(input("请输入一点坐标："))
x2,y2=eval(input("请输入另一个点坐标："))
print(x1,y1)
print(x2,y2)

turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.write("("+str(x1)+","+str(y1)+")")

turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.goto(x2,y2)
turtle.write("("+str(x2)+", "+str(y2)+")")
turtle.hideturtle()
turtle.done()