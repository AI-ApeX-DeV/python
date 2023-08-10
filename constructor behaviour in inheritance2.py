class a:

    def __init__(self):
        print("in a init")

    def b(self):
        print("This is b")


class b:

    def __init__(self):
        print("in b init")

    def b(self):
        print("This is b")


class c(a, b):

    def __init__(self):
        super().__init__()
        print("in c init")

    def c(self):
        print("This is c")


ob = c()
