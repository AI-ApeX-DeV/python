a = 10
b = 6
c = 9


def functionn():
    b = 8
    print(b)
    global a
    a = 15
    b = 11


functionn()
print(a)
print(b)
print(c)
