import re

num_cases = int(input())

for i in range(num_cases):
    match = re.fullmatch(r'^[+-]?[\d]*\.+[\d]+$', input())
    if match:
        print(True)
    else:
        print(False)
