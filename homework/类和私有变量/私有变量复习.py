class money:
    def __init__(self):
        self.__money=100
    def show(self):
        print(self.__money)
李欣的钱=money()
李欣的钱.__money=-10000
print(李欣的钱.__money)
李欣的钱.show()