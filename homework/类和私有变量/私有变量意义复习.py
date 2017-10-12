class money:
    def __init__(self):
        self.__money=100
    def show(self):
        print(self.__money)
    def 存款(self,num):
        self.__money+=num
        self.show()
    def 取款(self,num,password):
        if password=="123456":
            self.__money-=num
            self.show()
        else:
            print("密码错误请重新输入")
    def 查询(self,password):
        if password=="123456":
            return self.__money
        else:
            print("密码错误请重新输入")
            return None
LQ=money()
LQ.存款(1000)
LQ.取款(1000,"123456")
print(LQ.查询("123456"))
LQ.__money=-100000000
print(LQ.查询("123456"))
