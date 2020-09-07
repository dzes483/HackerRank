import numpy

n, m = [int(i) for i in input().split()]
list_a, list_b = [], []

for num in range(n):
    list_a.append([int(i) for i in input().split()])
for num in range(n):
    list_b.append([int(i) for i in input().split()])

args = ['add', 'subtract', 'multiply', 'divide', 'mod', 'power']
for arg in args:
    if arg == 'divide':
        print(numpy.array(list_a)//numpy.array(list_b))
    else:
        print(getattr(numpy, arg)(numpy.array(list_a), (numpy.array(list_b))))
