class students:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class laptop:

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = students('Rahul', 2)
s2 = students('Rohit', 3)

s1.show()

print(s1.lap.brand, s1.lap.cpu, s1.lap.ram, s1.name, s1.rollno)
