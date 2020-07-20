import re

num_cases = int(input())

for i in range(num_cases):
    m = re.fullmatch(r'^[+-]?[\d]*\.+[\d]+$', input())
    if m:
        print(True)
    else:
        print(False)
