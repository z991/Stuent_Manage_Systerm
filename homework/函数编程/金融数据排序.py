import csv
import operator
reader=csv.reader(open(r"H:\DAY\day25\code\000001.csv","r"))
alllist=[]
for item in reader:
    alllist.append(item)
alllist.sort(key=operator.itemgetter(3))
alllist.reverse()
for line in alllist:
    print(line)