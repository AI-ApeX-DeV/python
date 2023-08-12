nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = iter(nums)

print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())


class syed:

    def move(self, a):
        a = iter(a)
        return a.__next__()

    def loop(self, array, first, last):
        if first <= last:
            print(array[first])
            first += 1
            self.loop(array, first, last)


print("inside a class work")
ob = syed()
print(ob.move(nums))

ob.loop(nums, 0, 9)
