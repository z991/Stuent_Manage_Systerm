import time
mytimes=time.time()
print(mytimes)
print("自从1970年现在过去了",int(mytimes),"秒")
seconds=mytimes%60
hours=int(mytimes)//3600
mins=(int(mytimes)-int(mytimes)//3600*3600)
mins=(mins-seconds)//60
print("自从1970年现在过去了",
      hours,"小时",
       mins,"分钟",
       seconds,"秒")


