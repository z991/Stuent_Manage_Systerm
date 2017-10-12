import pymysql

class XuanSql():
    def __init__(self,host,user,password,dbName):
        self.host=host
        self.user=user
        self.password=password
        self.dbName=dbName
    def connet(self):
        self.db=pymysql.connect(self.host,self.user,self.password,self.dbName)
        self.cursor=self.db.cursor()
    #释放
    def close(self):
        self.cursor.close()
        self.db.close()

    def get_one(self,sql):
        res=None#结果
        try:
            self.connet()
            self.cursor.execute(sql)
            res=self.cursor.fetchone()
            self.close()
        except:
            print("查询失败")
        return  res
    def get_all(self,sql):
        res=()
        res = None  # 结果
        try:
            self.connet()
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            self.close()
        except:
            print("查询失败")
        return res
    def insert(self,sql):
        return self.__edit(sql)
    def update(self,sql):
        return self.__edit(sql)
    def delete(self,sql):
        return self.__edit(sql)

    def __edit(self,sql):
        count=0
        try:
            self.connet()
            count=self.cursor.execute(sql)
            self.db.commit()
            self.close()
        except:
            print("事务提交失败")
            self.db.rollback()
        return count