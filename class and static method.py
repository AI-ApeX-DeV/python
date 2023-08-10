class students:

    school = "ABC School"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod
    def getSchool(cls):   # cls is class variable
        cls.school = "XYZ School"
        return cls.school

    # @staticmethod
    def info():
        print("This is students class... in abc module")


s1 = students(34, 67, 32)
s2 = students(89, 32, 12)

print(s1.avg())
print(s2.avg())
print(s1.school)

print(students.getSchool())

print(s1.school)

students.info()
s1.info()
