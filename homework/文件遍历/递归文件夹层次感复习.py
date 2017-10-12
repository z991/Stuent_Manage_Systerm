'''import os
def getall(path,treeshow):
    filelist=os.listdir(path)
    for filename in filelist:
        filepath=os.path.join(path,filename)
        if os.path.isdir(filepath):
            print(treeshow,"文件夹",filename)
            treeshow+="     "
            getall(filepath,treeshow)
        else:
            print(treeshow,"文件",filename)
getall(r"F:\\大数据\\通讯录","")'''


import os

def  getall(path,treeshow):
    filelist=os.listdir(path)
    for  filename in filelist:
        filepath=os.path.join(path,filename)#完整路径
        if os.path.isdir(filepath):
            print(treeshow,"文件夹", filename)
            treeshow += "   "
            getall(filepath,treeshow)
        else:
            print(treeshow,"文件",filename)


getall(r"F:\\大数据\\通讯录","")