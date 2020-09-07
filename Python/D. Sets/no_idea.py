n, m = [int(i) for i in input().split()]
arr = [int(i) for i in input().split()]
a = set([int(i) for i in input().split()])
b = set([int(i) for i in input().split()])
happiness = 0
for i in arr:
    if i in a:
        happiness += 1
    elif i in b:
        happiness -= 1

print(happiness)
