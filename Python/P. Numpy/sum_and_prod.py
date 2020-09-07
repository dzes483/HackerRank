import numpy

n, m = [int(i) for i in input().split()]

l = []
for _ in range(n):
    ints = [int(i) for i in input().split()]
    l.append(ints)

print(numpy.prod(numpy.sum(numpy.array(l), axis=0)))
