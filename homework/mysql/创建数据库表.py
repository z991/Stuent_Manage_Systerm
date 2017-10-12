import pymysql
#连接数据库
db=pymysql.connect("192.168.154.1",
                   "root",
                   "111111",
                   "kaige")
#创建一个cursort对象
cursor=db.cursor()
sql='create table bandcard(id int auto_increment primary key,money int not null )'
cursor.execute(sql)
#断开
cursor.close()
db.close()