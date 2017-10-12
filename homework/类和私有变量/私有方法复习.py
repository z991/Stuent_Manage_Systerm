class money:
    def __init__(self):
        self.__money=100
    def __getmoney(self):
        return self.__money
    def __setmoney(self,num):
        self.__money=num
    def __checkpass (self,password):
        if password=="123456":
            return True
        else:
            return False
    def 查询(self,password):
        if self.__checkpass(password):
            return self.__getmoney()
        else:
            return None
林欣的钱=money()
print(dir(林欣的钱))
print(林欣的钱.查询("123456"))