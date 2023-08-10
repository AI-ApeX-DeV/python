class a:
    def show(self):
        print("in a show")


class b:
    def show(self):
        print("in b show")


class c(a, b):
    pass


ob = c()
ob.show()


class d:
    def show(self):
        print("in d show")


class e(d):

    def show(self):
        print("in e show")


ob = e()
ob.show()
