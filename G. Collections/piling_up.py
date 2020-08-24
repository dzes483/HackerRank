from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    ints = deque([int(i) for i in input().split()])
    for _ in range(len(ints)-1):
        if ints[0] >= ints[1]:
            ints.popleft()
        elif ints[-1] >= ints[-2]:
            ints.pop()
    if len(ints) == 1:
        print("Yes")
    else:
        print("No")
