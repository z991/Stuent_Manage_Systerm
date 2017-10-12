month=eval(input("请输入月份"))
years=eval(input("请输入年份"))
if month==1:
    print("31天")
elif month==2:
    if (years%4==0 and years%100!=0) or (years%400==0):
        print("29天")
    else:
        print("28天")
elif month==3:
    print("31天")
elif month==4:
    print("30天")
elif month==5:
    print("31天")
elif month==6:
    print("30天")
elif month==7:
    print("31天")
elif month==8:
    print("31天")
elif month==9:
    print("30天")
elif month==10:
    print("31天")
elif month==11:
    print("30天")
elif month==12:
    print("31天")
else:
    print("脑袋有泡")