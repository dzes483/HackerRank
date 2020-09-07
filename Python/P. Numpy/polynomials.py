import numpy

coefs = [float(i) for i in input().split()]
x = int(input())

print(numpy.polyval(coefs, x))
