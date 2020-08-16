import numpy

n, m = [int(i) for i in input().split()]

arr = []

for _ in range(n):
    arr.append([int(i) for i in input().split()])
min = numpy.min(numpy.array(arr), axis=1)
print(numpy.max(min))
