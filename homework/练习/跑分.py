import time
#1，100000000  跑分

starttime=time.time() #开始时间
#跑分代码
lastnum=0
num=0  #1-》100000000
while num<100000000:
    num+=1
    lastnum+=num
print(lastnum)#最终数值
endtime=time.time()#结束时间
print(endtime-starttime)#时间差