num=lambda a,b:a+b
print(num(1,2))

num3=lambda a,b,c:a+b+c
print(num3(1,2,3))

print((lambda a,b:a+b)(20,30))
print((lambda a,b:a+b)(30,50))#匿名调用

(lambda mystr:print(str)("hellow world"))