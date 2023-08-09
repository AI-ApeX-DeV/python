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


arr = zeros(5, int)
print(arr)

# multi dimensional array
arr = array([[1, 2, 3], [4, 5, 6]])
print(arr)

print(arr.dtype)
print(arr.ndim)
print(arr.shape)
print(arr.size)

arr = arr.flatten()
print(arr)

arr = arr.reshape(3, 2)
print(arr)

m = matrix(arr)
print(m)

m = matrix('1 2 3; 4 5 6; 7 8 9')
print(m)

print(diagonal(m))

m1 = matrix('1 2 3; 4 5 6; 7 8 9')
m2 = matrix('1 2 3; 4 5 6; 7 8 9')
m3 = m1+m2
print(m3)

m3 = m1*m2
print(m3)

m3 = m1-m2
print(m3)

m3 = m1/m2
print(m3)

m3 = m1 % m2
print(m3)


a = array('i', [])
n = int(input("Enter the length of the array: "))

for i in range(n):
    x = int(input("Enter the next value: "))
    a.append(x)

print(a)
