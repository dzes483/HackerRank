import numpy


n, m, p = [int(i) for i in input().split()]
l_1 = []
l_2 = []

for num in range(n):
    p_arr_1 = [int(i) for i in input().split()]
    l_1.append(p_arr_1)

for num in range(m):
    p_arr_2 = [int(i) for i in input().split()]
    l_2.append(p_arr_2)

print(numpy.concatenate((numpy.array(l_1), numpy.array(l_2))))
