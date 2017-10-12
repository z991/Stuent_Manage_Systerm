import ftplib
try:
    myftp=ftplib.FTP("hk801.pc51.com")

    myftp.login("user","password")
    print("密码正确")

except:
        print("密码不正确")