a,b,c,d,e,f,=eval(input("请输入a,b,c,d,e,f"))
if a*d-b*c==0:
    print("The equation has no solution")
else:
    print("x is",(e*d-b*f)/(a*d-b*c),"and","y is ",(a*f-e*c)/(a*d-b*c)          )