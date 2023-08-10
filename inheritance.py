class a:

    def a(self):
        print("This is a")

    def b(self):
        print("This is b")


class b(a):

    def c(self):
        print("This is c")

    def d(self):
        print("This is d")


class c(b):

    def e(self):
        print("This is e")

    def f(self):
        print("This is f")


ob = c()
ob.a()
ob.b()
ob.c()
ob.d()
ob.e()
ob.f()
