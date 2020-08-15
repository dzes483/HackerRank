import numpy

arr = numpy.array([float(i) for i in input().split()])
numpy.set_printoptions(sign=' ')
print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))
