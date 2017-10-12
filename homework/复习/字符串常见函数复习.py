mystr="hello python2 hello world3"
print(mystr.capitalize())#第一个字符转化为大写

mystr="8888"
for i in range(6,40,2):
    for j in range((40-i)//2,0,-1):
        print(" ",end="")
    print(mystr.center(i,'*'))
