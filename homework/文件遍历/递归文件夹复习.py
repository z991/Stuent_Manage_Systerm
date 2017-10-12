'''import os
filelist=os.listdir("F:\\大数据\\通讯录")
#print(filelist)
for file  in filelist:
    if os.path.isdir("F:\\大数据\\通讯录\\"+file):
        print("文件夹",file)
    else:
        print("文件", file)
'''
import os
def getall(path):
    filelist=os.listdir(path)
    for filename in filelist:
        filepath=os.path.join(path,filename)
        if os.path.isdir(filepath):
            print("文件夹",filename)
            getall(filepath)
        else:
            print("文件",filename)
getall(r"F:\\大数据\\通讯录")