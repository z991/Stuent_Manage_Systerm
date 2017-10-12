'''for num in range(0,100):
    if num%2==0:
        continue
    print(num)
    num=0
while num<100:
    print(num)
    num=num+1
    if num%2==0:
        continue'''

num=0
while num<10000:
    num=num+1
    if num%2==0:
        continue
    if num>100:
        break
    print(num)