class printing():

    def config(self):
        print("I am printing")


ob = printing()
ob.config()
printing.config(ob)


class Computer:

    fans = 2

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is ", self.cpu, self.ram)

    def compare(self, other):
        if self.cpu == other.cpu and self.ram == other.ram:
            return True
        else:
            return False


com1 = Computer('i5', 16)
com2 = Computer('Ryzen 3', 8)


com1.config()
com2.config()

com1.cpu = 'i7'
com1.config()


if com1.compare(com2):
    print("They are same")
else:
    print("They are different")


print(com1.fans, com2.fans)

Computer.fans = 3

print(com1.fans, com2.fans)

com1.fans = 4

print(com1.fans, com2.fans)
