import re

s = input()
k = input()
regex = re.compile(rf"(?=({k}))")
results = [i for i in re.finditer(regex, s)]

if len(results) > 0:
    for i in re.finditer(regex, s):
        print((i.start(), i.start() + len(k)-1))
else:
    print((-1, -1))
