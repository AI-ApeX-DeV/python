from array import *
vals = array('i', [1, 2, 3, 4, 5, 6])
print(vals)
vals.reverse()
print(vals)
print(vals.buffer_info())
print(vals.typecode)
print(vals[0])
