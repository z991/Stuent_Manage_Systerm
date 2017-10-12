import os
path=r"F:\\大数据\\通讯录"
mystack=[]
mystack.append(path)
while len(mystack)!=0:
    path=mystack.pop()
    filelist=os.listdir(path)
    print(filelist)
    for filename in filelist:
        filepath=os.path.join(path,filename)
        if os.path.isdir(filepath):
            print("文件夹",filename)
            print(filepath)
            mystack.append(filepath)
        else:
            print("文件",filename)