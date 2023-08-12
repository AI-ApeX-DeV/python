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
f.close()

print("lets explore something different\n")

f = open("data.txt", "w")
f.write("this is a new line\n this is the second line\n this is the third line\n this is the fourth line\n")
f.close()

print("lets explore something different\n")

f = open("data.txt", "r")
print(f.read())
f.close()

print("lets explore something different\n")

f = open("data.txt", "a")
f.write("this is the fifth line\n")
f.close()

print("lets explore something different\n")

f = open("data.txt", "r")
print(f.read())
f.close()
