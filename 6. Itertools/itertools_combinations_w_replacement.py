from itertools import combinations_with_replacement

string, size = [i for i in (input().split())]
combos = combinations_with_replacement(sorted(string), int(size))

for i in combos:
    print(''.join(i))
