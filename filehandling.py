f = open("data.txt", "r")
# even here in case of read there is a pointer which keeps moving line by line
print(f.read())
print("lets explore something different")
f.close()
f = open("data.txt", "r")
print(f.readline())
print(f.readline())
print(f.readline())

print(f.readline(4))
