import re

num_test_cases = int(input())
for num in range(num_test_cases):
    s = input()
    try:
        regex = re.compile(s)
        print(True)
    except Exception:
        print(False)
