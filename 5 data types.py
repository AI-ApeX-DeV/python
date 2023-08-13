num = 2.5
print(type(num))

num = 2+3j
print(type(num))

num = 2
print(type(num))

num = True
print(type(num))

num = 6.7
print(type(num))

a = int(num)
print(a)
print(type(a))

c = complex(num, a)
print(c)
print(type(c))

a = (1, 2)
print(type(a))

a = [1, 2]
print(type(a))

a = {1, 2}
print(type(a))

a = {1: 2}
print(type(a))

a = "string"
print(type(a))

print(list(range(10)))
print(list(range(1, 10)))
print(list(range(1, 10, 2)))
