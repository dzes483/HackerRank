import numpy

n, m = [int(i) for i in input().split()]

li = []

for num in range(n):
    li.append([int(i) for i in input().split()])

print(numpy.array(li).transpose())
print(numpy.array(li).flatten())
