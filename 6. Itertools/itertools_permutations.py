from itertools import permutations

string, size = [i for i in (input().split())]
size = int(size)
perms = permutations(string, size)

for i in sorted(perms):
    print(''.join(i))
