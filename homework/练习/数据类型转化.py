
'''
print(int("12")) #转化为整数
print(str(12)) #转化为字符串
print(float("1.5678")) #字符串转化浮点数
print(list((1,2,3,4))) #元祖
print([1,2,3,4,5]) #集合
print(tuple([1,2,3,4,5]))#数据类型转换tuple
print(set([1,2,3,4,5])) #，集合
print(repr(1+2*3+4)) #算法
'''

print(int("16",10))   #
print(int("16",8)) #按照进制转化
print(hex(100))#6*16^1=96  +4*16^0=4=100
print(oct(10)) #1*8^1+2*8^0
mylist=[1,2,3]
myset=frozenset(mylist) #转变为不可变集合
mylist[0]=100
#myset[0]=100 #set，不支持索引，tuple,list
print(mylist)
print(myset)
