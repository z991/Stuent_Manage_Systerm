def go():
    print(1)
    yield 15
    print(2)
    yield 28
    print(3)
    yield 45
X=go()
print(next(X))
print(next(X))
print(next(X))
