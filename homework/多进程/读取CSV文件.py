import csv
path=r"D:\朱烜宇\day23down\csv\000001.csv"
reader=csv.reader(open(path,"r"))
for item in reader:
    for data in item:
        print(data)