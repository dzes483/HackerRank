import re

def solve(s):
    s = re.split("( )", s)
    new_str = []
    for item in s:
        new_str.append(item.capitalize())
    return ''.join(new_str)
if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
