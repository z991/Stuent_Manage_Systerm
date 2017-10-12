num=5
filesplitlist=[]
for i in range(num):
    filepath=r"E:\70G\52G葫芦娃\1632\163切割\data"+str(i)+".txt"
    file=open(filepath,"wb")
    filesplitlist.apppend(file)
fileallpath=r"E:\70G\52G葫芦娃\1632\bigdata.txt"
fileall=open(fileallpath,"rb")
i=0
for line in fileall:
    filesplitlist[i%num].write(line)
    i+=1

fileall.close()
for i in range(num):
    filesplitlist[i].close