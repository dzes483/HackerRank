import re

for num in range(int(input())):
    result = re.fullmatch(r"^[789]\d{9}", input())
    if result:
        print('YES')
    else:
        print('NO')
