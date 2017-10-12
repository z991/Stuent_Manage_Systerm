class SweetPotato:
    def __init__(self):
        self.cookedString="生的"
        self.cookedLevel=0
        self.condiments=[]
    def __str__(self):
        return "地瓜 状态:%s(%d),添加的佐料有：%s"%(self.cookedString,self.cookedLevel,str(self.condiments))
    def cook(self,cooked_time):
        self.cookedLevel += cooked_time

        if self.cookedLevel>=0 and self.cookedLevel<3:
            self.cookedString="生的"
        elif self.cookedLevel>=3 and self.cookedLevel<5:
            self.cookedString = "半生不熟"
        elif self.cookedLevel>= 5 and self.cookedLevel < 8:
            self.cookedString = "熟了"
        else:
            self.cookedString = "考糊了"
    def addcondiments(self,item):
        self.condiments.append(item)
        pass

di_gua=SweetPotato()
print(di_gua)

di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
di_gua.addcondiments("大蒜")
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
di_gua.addcondiments("番茄酱 ")
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)