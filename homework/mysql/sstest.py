from xuanSql import XuanSql
s=XuanSql("192.168.154.1",
                   "root",
                   "111111",
                   "kaige")
res=s.get_all("select * from bandcard WHERE money>600")
for row in res:
    print("%d--%d" % (row[0],row[1]))