import csv
def gettotoal(path):
    reader=csv.reader(open(path,"r"))
    num=0
    alldata=0
    for item in reader:
        if num==0:
            pass
        else:
            alldata+=eval(item[13])
        num+=1
    return alldata/num
path=r"H:\DAY\day23down\csv\000001.csv"
print(gettotoal(path))