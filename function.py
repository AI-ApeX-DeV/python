def change(a):
    x = a
    print("id of x", id(x))
    x = 15
    print("id of x", id(x))


a = 10
print("id of a", id(a))
change(a)
print(a)


def listchange(a):
    print("id of a", id(a))
    a[1] = 15
    print("id of a", id(a))


a = [10, 20, 30]
print("id of a", id(a))
listchange(a)
print(a)
