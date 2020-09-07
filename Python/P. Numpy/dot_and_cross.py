import numpy

n = int(input())
arr_a, arr_b = [], []
for _ in range(n):
    arr_a.append([int(i) for i in input().split()])
for _ in range(n):
    arr_b.append([int(i) for i in input().split()])

print(numpy.dot(arr_a, arr_b))
