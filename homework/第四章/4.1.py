'''a,b,c=eval(input("请输入a,b,c"))
if b*b-4*a*c>0:
    print("The roots are",round((-b+    (b*b-4*a*c)    **0.5)/2/a,6),
                           round((-b-    (b*b-4*a*c)    **0.5)/2/a,5 )   )
elif b*b-4*a*c==0:
    print("The root is",round((-b+    (b*b-4*a*c)    **0.5)/2/a,6))
else:
    print("The equation has no real roots" )'''
a,b,c=eval(input("请输入a,b,c"))
#ax*x+bx+c=0
if a==0:
    if b==0:
        if c==0:
            print("x为任意数")
        else:
            print("x无解")
else:
    dt=b*b-4*a*c
    if dt>0:
        print("x1=", (-b + dt ** 0.5) / (2 * a), ",x2=", (-b - dt ** 0.5) / (2 * a))
    elif dt==0:
        print("x1=x2", (-b + dt ** 0.5) / (2 * a))
    else:
        print("x1=", -1 * b / 2 / a, "+", (-1 * dt) ** 0.5 / (2 * a), "i")
        print("x2=", -1 * b / 2 / a, "-", (-1 * dt) ** 0.5 / (2 * a), "i")



