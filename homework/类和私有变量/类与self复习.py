class 懒人类:
    name="李白"#属性-变量 self可以调用属性
    def 懒(self):#行为-函数，self用于区分谁调用的
        print(self.name,"爱睡觉")#属性一般要加self
        self.go()#self只能在类的内部，只能在内部，不能在外部
    def go (self):
        print("self addr",id(self))
        print("我很懒，不想动")
李白=懒人类()
print(type(李白))
print(李白.name)


李白.懒()

杜甫=懒人类()
杜甫.name="杜甫"
print("杜甫addr",id(杜甫))
杜甫.go()
print(id(杜甫.name),id(李白.name))
print(id(杜甫.go()),id(李白.go))
#self本质就是实例化以后的对象地址
#self可以调用类的属性，类的方法
#类中，属性格子独立，方法是共享的，调用传递self,区别谁调用的