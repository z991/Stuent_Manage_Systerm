import os
path=r"F:\\大数据\\通讯录"
mystack=[]
mystack.append([path,0])
while len(mystack)!=0:
    pathlist=mystack.pop()
    filelist=os.listdir(pathlist[0])
    num=pathlist[1]
    headstr=""
    for i in range(num):
        headstr+="     "
    for i in range(len(filelist)):
        filename=filelist[len(filelist)-1-i]
        filepath=os.path.join(pathlist[0],filename)
        if os.path.isdir(filepath):
            print(headstr,"文件夹",filepath)
            mystack.append([filepath,num+1])
        else:
            print(headstr,"文件",filepath)