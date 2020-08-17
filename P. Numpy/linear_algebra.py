import numpy

n = int(input())

arr_a = []
for _ in range(n):
    arr_a.append([float(i) for i in input().split()])

arr_a = numpy.array(arr_a)

print(numpy.around(numpy.linalg.det(arr_a), decimals=2))
