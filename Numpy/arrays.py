import numpy

def arrays(arr):
    a = numpy.array(arr, dtype=numpy.float64)
    b = numpy.flip(a)
    return b

arr = input().strip().split(' ')
result = arrays(arr)
print(result)