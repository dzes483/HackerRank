num_elems = int(input())
s = set([int(i) for i in (input().split())])
num_cmds = int(input())

for i in range(num_cmds):
    args = input().split()
    if args[0] == 'pop':
        getattr(s, args[0])()
    else:
        getattr(s, args[0])(int(args[1]))
print(sum(s))
