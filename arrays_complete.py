import array as arr  # from numpy import *
from numpy import *
vals = arr.array('i', [1, 2, 3, 4, 5, 6])
print(vals)
vals.reverse()
print(vals)
print(vals.buffer_info())  # (address, size)
print(vals.typecode)
print(vals[0])

a = linspace(0, 15, 16)
print(a)
a = logspace(0, 15, 16)
print(a)
a = 2.5432234
print(a)
print('%.2f' % a)

arr = ones(5, int)
print(arr)

a = arr+5
print(a)

print(a+arr)

print(sin(a))
print(cos(a))
print(log(a))
print(sqrt(a))

print(concatenate([a, arr]))

# shallow copy and deep copy

# shallow copy
print("ARRAY", arr)
arr1 = arr.view()
arr2 = arr.copy()
arr[1] = 7


print("shadow copy", arr1)
print("deep copy", arr2)

# deep copy


arr = zeros(5, int)
print(arr)

a = array('i', [])
n = int(input("Enter the length of the array: "))

for i in range(n):
    x = int(input("Enter the next value: "))
    a.append(x)

print(a)
