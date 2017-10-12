num=eval(input("请输入数据数量"))
print(num)

maxdata=eval(input("data"))
print(maxdata)
for i in range(num-1):
    data=eval(input("data"))
    if data>maxdata:
        maxdata=data
    print(data)
print("max",maxdata)