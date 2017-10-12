import os.path
import sys

def main():
    keyWords={"and","as","assert","break","class","continue","def","del","elif","else",
              "except","False","finally","for","from","global","if","import","in","is",
              "lambda","None","nonlocal","not","or","pass","raise","return","True","try",
              "while","whith","yield"}
    filename=input("Enter a Python source code filename:").strip()
    if not os.path.isfile(filename):
        print("File",filename,"does not exist")
        sys.exit
    infile=open(filename,"r")
    text=infile.read().split()
    count=0
    for word in text:
        if word in keyWords:
            count+=1
    print("The number of keywords in",filename,"is",count)
    main()

