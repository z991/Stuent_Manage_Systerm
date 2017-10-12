class namemoney:
    def __init__(self):
        print("构造了",id(self))
    def __del__(self):
        print("删除了",id(self))
zhangsan=namemoney()
lisi=namemoney()

