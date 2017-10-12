a=eval(input("请输入代表今天的数字"))
b=eval(input("请输入未来某天的天数"))
c=(a+b)%7
if a==0:
    print("今天是周日")
elif a==1:
    print("今天是周一")
elif a == 2:
    print("今天是周二")
elif a == 3:
    print("今天是周三")
elif a==4:
    print("今天是周四")
elif a==5:
    print("今天是周五")
elif a==6:
    print("今天是周六")
if c==0:
    print("未来这天是周日")
elif c==1:
    print("未来这天是周一")
elif c == 2:
    print("未来这天是周二")
elif c == 3:
    print("未来这天是周三")
elif c==4:
    print("未来这天是周四")
elif c==5:
    print("未来这天是周五")
elif c==6:
    print("未来这天是周六")
