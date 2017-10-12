a,b,c=eval(input("请输入三个整数"))
if a>b:
    if a>c:
        print("max",a)
        if b>c:
            print(c,b,a)
        else:
            print(b,c,a)
    if a<c:
        print("max",c)
        print(c,b,a)
else:
    if b>c:
        print("max",b)
        if a>c:
            print(c,a,b)
        else :
            print(a,c,b)
    if b<c:
        print("max",c)
        print(a,b,c)