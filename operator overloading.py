class student:

    def marks(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = student()
        s3.marks(m1, m2)
        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False


a = student()
b = student()
a.marks(10, 20)
b.marks(20, 30)

c = a+b
print(c.m1)
print(c.m2)

if a > b:
    print("a wins")
else:
    print("b wins")
