a = ['navin', 'kiran', 'harsh', 'navin']
b = ['python', 'java', 'c', 'python']

c = zip(a, b)
print(c)


c = list(zip(a, b))
print(c)

c = tuple(zip(a, b))
print(c)

c = set(zip(a, b))
print(c)

c = dict(zip(a, b))
print(c)
