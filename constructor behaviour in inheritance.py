class a:

    def __init__(self):
        print("in a init")

    def a(self):
        print("This is a")


class b(a):

    def __init__(self):
        print("in b init")

    def b(self):
        print("This is b")


class c(b):

    def __init__(self):
        super().__init__()
        print("in c init")

    def c(self):
        print("This is c")


ob = c()
