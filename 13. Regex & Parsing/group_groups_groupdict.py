import re

s = input()
result = 0

for i in s:
    if i.isalnum():
        try:
            m = re.search(r"([{}])(?=([{}]))".format(i, i), s)
            if m.group(2):
                print(i)
                result = 0
                break
        except AttributeError:
            result = -1
            continue

if result == -1:
    print(result)
