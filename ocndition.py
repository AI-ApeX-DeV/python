a = 5
if a == 5:
    print("a is equal to 5")
elif a == 6:
    print("a is equal to 6")
else:
    print("a is not equal to 5 or 6")


for i in range(1, 10, 2):
    print(i, end=" ")

i = 0
print()

while i < 10:
    print(i, end=" ")
    i += 1

print()

for i in range(10):
    if i == 5:
        print("this is 5", end=" ")
        continue
        print("this is cool")
    elif i == 6:
        pass
    elif i == 7:
        print("this is 7", end=" ")
        pass
        print("this is cool", end=" ")
    elif i == 8:
        print("this is 8 now its time to end the loop", end=" ")
        break
    else:
        print(i, end=" ")
