def farg(*args):
    for i in args:
        print(i)


def fkwarg(**kwargs):
    for key, value in kwargs.items():
        print("{}:{}".format(key, value))


def fargkwarg(*args, **kwargs):
    for i in args:
        print(i)
    for key, value in kwargs.items():
        print("{}:{}".format(key, value))


farg(1, 2, 3, 4, 5)
fkwarg(name="Navin", age=28, mob=1234567890)
fargkwarg(1, 2, 3, 4, 5, name="Navin", age=28, mob=1234567890)
