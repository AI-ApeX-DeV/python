data = {1: 'Navin', 2: 'Kiran', 3: 'Harsh', 4: 'Rahul'}
print(data)

print(data[1])

print(data.get(1))

print(data.get(5))

print(data.get(5, 'Not Found'))

print(data.keys())

print(data.values())

print(data.items())

a = [1, 2, 3, 4, 5]
b = ["navin", "kiran", "harsh", "rahul", "kirrr"]
c = dict(zip(a, b))

print(c)

c[3] = [1, 2, 3, 4, 5]

print(c)


c[3] = {1: 'Navin', 2: 'Kiran', 3: 'Harsh', 4: 'Rahul'}

print(c)
