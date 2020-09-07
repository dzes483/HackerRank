num_elems = int(input())
set_a = set([int(i) for i in (input().split())])
num_sets = int(input())

for i in range(num_sets):
    args = input().split()
    elems = set([int(i) for i in (input().split())])
    getattr(set_a, args[0])(elems)

print(sum(set_a))
