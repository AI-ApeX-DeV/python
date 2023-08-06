a = [1, 2, 3, 4, "list", "python", 55, 67]
print(a[0:4])
print(a[4:6])
print(a[1:])
print(a[:6])
print(a[1:6:2])
print(a[-1])

a.clear()
print(a)

a.insert(0, 1)
a.insert(1, 2)
a.insert(2, 3)
a.insert(3, 4)
a.insert(4, 9)
a.insert(5, 8)
a.insert(6, 7)
print(a)

a.remove(2)

print(a)

a.pop(1)
print(a)

a.append(2)
print(a)

a.reverse()
print(a)

a.sort()
print(a)

a.sort(reverse=True)
print(a)

a.pop()
print(a)

a.extend([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(a)

print(min(a))
print(max(a))
print(sum(a))
print(len(a))
print(a.count(2))
print(a.index(2))
# 1 is the element, 1 is the starting index, 10 is the ending index
print(a.index(2, 5, 10))
