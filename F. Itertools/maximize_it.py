from itertools import product

k, m = [int(i) for i in input().split()]
l = []
for _ in range(k):
    s = list(map(int, input().split()[1:]))
    l.append(list(i**2 for i in s))
print(max(list(sum(j)%m for j in product(*l))))
