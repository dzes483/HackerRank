from collections import deque

num_ops = int(input())
d = deque()

for num in range(num_ops):
    args = input().split()
    if len(args) == 1:
        getattr(d, args[0])()
    else:
        getattr(d, args[0])(int(args[1]))
print(i for i in d)
