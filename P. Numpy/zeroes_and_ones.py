import numpy

arr = numpy.array([int(i) for i in input().split()])

print(numpy.zeros(arr, dtype=numpy.int))
print(numpy.ones(arr, dtype=numpy.int))
