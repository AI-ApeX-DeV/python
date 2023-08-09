from array import *  # from numpy import *
vals = array('i', [1, 2, 3, 4, 5, 6])
print(vals)
vals.reverse()
print(vals)
print(vals.buffer_info())  # (address, size)
print(vals.typecode)
print(vals[0])


a = array('i', [])
n = int(input("Enter the length of the array: "))

for i in range(n):
    x = int(input("Enter the next value: "))
    a.append(x)

print(a)
