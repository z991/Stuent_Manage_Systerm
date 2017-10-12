class Accound:
    def __init__(self, id=0, balance=100, annualInterestRate=0):
        self.__id = id
        self.__balance = float(balance)
        self.__annualInterestRate = float(annualInterestRate)
    def getid(self):
        return self.__id
    def getbalance(self):
        return self.__balance
    def getannualInterestRate(self):
        return self.__annualInterestRate
    def setid(self,id):
        self.__id=id
    def setbalance(self,balance):
        self.__balance=balance
    def setannualInterestRate(self,annualInterestRate):
        self.__annualInterestRate=annualInterestRate
    def getMonthlyInterestRate(self):
        return self.__balance*self.__annualInterestRate/1200
    def withdraw(self, num):
        self.setbalance(self.__balance-num)
    def deposit(self, num):
        self.setbalance(self.__balance+num)

xiaoming=Accound(1,10000,0.5)
xiaoming.withdraw(100)
xiaoming.deposit(1000)
print(xiaoming.getid(),"号用户的余额为",xiaoming.getbalance())
print(xiaoming.getid(),"号用户的月利息为",xiaoming.getMonthlyInterestRate())