from collections import OrderedDict
from pyexcel_xls import get_data
from pyexcel_xls import save_data
def readxls():
    path=r"H:\大数据\信息对称数据库\《2010年杭州市最新经销代理企业通讯名录数据库》(500条).xls"
    xlsdata=get_data(path)
    print(xlsdata)
    for sheet in xlsdata:

        mylist=(sheet,":",xlsdata[sheet])
        for line in mylist:
            print(line)

def  writexls(): #写入excel
    path="myself.xls"
    data=OrderedDict()#字典
    sheet_1=[]  #表格
    sheet_2 = [] #表格
    row1=["A","B","C"]
    row2=[1,2,3]
    sheet_1.append(row1)
    sheet_1.append(row2)
    sheet_2.append(row1)
    sheet_2.append(row2)

    data.update({"ABC":sheet_1})
    data.update({"XYZ": sheet_2})
    save_data(path,data)

writexls()
#readxls()