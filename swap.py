a = 5
b = 7

temp = a
a = b
b = temp

print("a: {} , b: {}".format(a, b))

a, b = b, a

print("a: {} , b: {}".format(a, b))

a = a+b
b = a-b
a = a-b

print("a: {} , b: {}".format(a, b))

a = a ^ b
b = a ^ b
a = a ^ b

print("a: {} , b: {}".format(a, b))
