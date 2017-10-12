import pymysql
#连接数据库

db=pymysql.connect("192.168.154.1",
                   "root",
                   "111111",
                   "kaige")
#创建一个cursort对象
cursor=db.cursor()
sql="select version()"

cursor.execute(sql)
#获取返回的信息
data=cursor.fetchone()
print(data)

#断开
cursor.close()
db.close()