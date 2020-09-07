
n, m = [int(i) for i in input().split()]
arr = []
for _ in range(n):
    elems = [int(i) for i in input().split()]
    arr.append(elems)
k = int(input())
arr.sort(key=lambda x: x[k])
for i in arr:
    print(*i)
