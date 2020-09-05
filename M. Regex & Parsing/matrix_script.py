import re

n, m = [int(i) for i in input().split()]


symbol_regex = re.compile(r"(?<=[A-Z0-9])([!@#$%&\s])+(?=[A-z0-9])", re.IGNORECASE)


matrix = []
for _ in range(n):
    matrix.append(input())

col = 0
result = []
while col < m:
    for i in matrix:
        for j in i[col]:
            result.append(j)
    col += 1
str = ''.join(result)
print(re.sub(symbol_regex, " ", str))
