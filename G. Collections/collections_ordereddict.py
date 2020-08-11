from collections import OrderedDict

num_items = int(input())
ordered_d = OrderedDict()

for i in range(num_items):
    args = [i for i in (input().split())]
    fruit = ' '.join(args[0:-1])
    price = int(args[-1])
    if fruit in ordered_d:
        ordered_d[fruit] += price
    else:
        ordered_d[fruit] = price

for k, v in ordered_d.items():
    print(f'{k} {v}')
