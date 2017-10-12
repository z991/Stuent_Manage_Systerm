import time
num=1.0
while num-10<0.000000001:
    num=num+0.1
    print(num)
    time.sleep(0.5)