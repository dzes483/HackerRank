from itertools import groupby

s = input()
for k, g in groupby(s, key=None):
    print(f"({len(list(g))}, {k}) ", end='')
