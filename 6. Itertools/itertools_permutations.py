from itertools import permutations

string, size = [i for i in (input().split())]
perms = permutations(string, int(size))

for i in sorted(perms):
    print(''.join(i))
