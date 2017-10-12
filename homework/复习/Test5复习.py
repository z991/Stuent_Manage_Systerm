import os
backosstystm=os.system


def check收费(mystr):
 if mystr.find("A")!=-1:
    backosstystm(mystr)
 else:
        print("请交保护费否则"+mystr+"无法执行")
os.system=check收费
os.system("echo Ahellowrld")
