import time
starttime=time.time()
num=0
while num<100000000:
    num=num+1
print(num)
endtime=time.time()
print(endtime-starttime)
