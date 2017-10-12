year=eval(input("请输入年份"))
if (year%4==0 and year%100!=0) or (year%400==0):
    print("这年是闰年")
else:
    print("这年不是闰年")