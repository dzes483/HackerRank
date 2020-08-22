import itertools

n = int(input())
l = [i for i in input().split()]
k = int(input())
combos = list(itertools.combinations(l[0:n], r=k))
a_count = 0
for i in combos:
    if 'a' in i:
        a_count += 1
print(round((a_count/len(combos)), 4))
