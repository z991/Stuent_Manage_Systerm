class datacompute:
    def __init__(self,x,y):
        print("create")
        self.a=x
        self.b=y
    def add(self):
        return self.a+self.b
d1=datacompute(100,1000)
print(d1.add())

d2=datacompute(200,1000)
print(d2.add())