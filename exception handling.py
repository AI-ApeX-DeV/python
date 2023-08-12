a = 5
b = 0

try:
    print(a/b)
except Exception as e:
    print("you can't divide a number by zero and the error is : ", e)

finally:
    print("resource closed")


try:
    a = int(input("enter a number"))

except Exception as e:
    print("invalid input and the error is : ", e)
