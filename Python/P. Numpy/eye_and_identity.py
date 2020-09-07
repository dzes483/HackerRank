import numpy

n, m = [int(i) for i in input().split()]
numpy.set_printoptions(sign=' ')

print(numpy.eye(n, m))
