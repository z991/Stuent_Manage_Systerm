import pymysql
#连接数据库
db=pymysql.connect("192.168.154.1",
                   "root",
                   "111111",
                   "kaige")
#创建一个cursort对象
cursor=db.cursor()
sql='insert into bandcard VALUES (0,300),(0,400),(0,800),(0,700),(0,1300),(0,2600),(0,3000),(0,12000)'
try:
    cursor.execute(sql)
    db.commit()
except:
    #如果提交失败会滚到上一次数据
    db.rollback()


#断开
cursor.close()
db.close()