from threading import *
from time import sleep


class wow1():

    def print(self):
        for i in range(100):
            print("wow1")
            sleep(0.1)


class wow2():

    def print(self):
        for i in range(100):
            print("wow2")
            sleep(0.1)


ob1 = wow1()
ob2 = wow2()

t1 = Thread(target=ob1.print)
t2 = Thread(target=ob2.print)

t1.start()
sleep(0.05)
t2.start()

t1.join()
t2.join()

print("bye")
