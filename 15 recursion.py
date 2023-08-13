import sys
i = 0
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)


def printh():
    global i
    i += 1
    print("Hello {}", i)
    printh()


printh()
