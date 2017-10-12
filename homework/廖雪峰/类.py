class Cat:
    def eat(self):
        print("吃鱼")
    def drink(self):
        print("喝水")
tom=Cat()
tom.eat()
tom.name="汤姆"
tom.age=40
tom.drink()

print("%s的年龄是：%d"%(tom.name,tom.age))