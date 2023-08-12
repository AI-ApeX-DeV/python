def topten():
    n = 1
    while n <= 10:
        sq = n * n
        yield sq
        n += 1


values = topten()
# to check if values is a iterator or not

if hasattr(values, '__iter__'):
    print("yes it is a iterator")

for i in topten():
    print(i)

    # or

for i in values:
    print(i)


def moveon():

    yield 2
    yield 3
    yield 4
    yield 5


print("move on")
for i in moveon():
    print(i)
