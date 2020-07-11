from collections import defaultdict

n, m = [int(num) for num in (input().split())]
d = defaultdict(list)

for int in range(n):
    d[input()].append(int+1)

group_b = [input() for j in range(m)]
for word in group_b:
    if word in d.keys():
        print(*d[word])
    else:
        print(-1)
