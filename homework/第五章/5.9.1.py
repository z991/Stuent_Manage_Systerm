'''num1=1000
num2=num1*1.05
num3=num2*1.05
num4=num3*1.05

#四年后总的学费
sum=num1+num2+num3+num4

i=0
sum=0
num=10000
while i<4:
    num=num*1.05
    i=i+1
    sum=num+sum
print(sum)


num=10000
for i in range(1,11):
    num=num*1.05
sum=num
for year in range(1,4):
    num=num*1.05
    sum=num+sum
print(sum)
'''
num=10000
i=1
while i<11:
    num=num*1.05
    i=i+1
sum=num
year=1
while year<4:
    num=num*1.05
    sum=sum+num
    year=year+1
print(sum)




