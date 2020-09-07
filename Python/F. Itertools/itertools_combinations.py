from itertools import combinations

string, size = [i for i in (input().split())]
combos = []

for num in range(int(size)+1):
    combos.append(combinations(sorted(string), num))
    for i in combos[num]:
        if i:
            print(''.join(i))
