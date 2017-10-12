num=eval(input("请输入数据数量"))
maxdata=eval(input("data"))
for i in range(num-1):

    data=eval(input("data"))
    if maxdata<data:
        maxdata=data
    print(data)
print("max",maxdata)
