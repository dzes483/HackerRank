import numpy

n, m = [int(i) for i in input().split()]

arr = []
for _ in range(n):
    arr.append([int(i) for i in input().split()])

numpy.set_printoptions(sign=' ')
print(numpy.mean(arr, axis=1))
print(numpy.var(arr, axis=0))
print(numpy.around(numpy.std(arr, axis=None), decimals=12))
