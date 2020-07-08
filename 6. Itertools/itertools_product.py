from itertools import product

a = [int(i) for i in (input().split())]
b = [int(i) for i in (input().split())]

result = tuple(product(a, b))

index = 0
for i in result:
    print(result[index], end=' ')
    index += 1
