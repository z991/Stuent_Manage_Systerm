import os
backosstystm=os.system


def check�շ�(mystr):
 if mystr.find("A")!=-1:
    backosstystm(mystr)
 else:
        print("�뽻�����ѷ���"+mystr+"�޷�ִ��")
os.system=check�շ�
os.system("echo Ahellowrld")
