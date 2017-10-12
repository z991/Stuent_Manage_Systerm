'''
fetchone()
功能：获取下一个查询结果集，结果集是一个对象


fetchall()
功能：接收全部的返回行

rowcount:是一个只读属性，返回execute()方法，影响行数
'''

import pymysql
#连接数据库
db=pymysql.connect("192.168.154.1",
                   "root",
                   "111111",
                   "kaige")
#创建一个cursort对象
cursor=db.cursor()
sql='select * from bandcard WHERE money>600'
try:
    cursor.execute(sql)
    relist=cursor.fetchall()
    for row in relist:
        print("%d--%d" % (row[0],row[1]))


except:
    #如果提交失败会滚到上一次数据
    db.rollback()

#断开
cursor.close()
db.close()