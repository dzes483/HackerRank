import re

pattern = re.compile(r"^(?!.*(\d)(-?\1){3})[4|5|6](\d{3})(-?\d{4}){3}$")

for _ in range(int(input())):
    result = re.fullmatch(pattern, input())
    if result:
        print("Valid")
    else:
        print("Invalid")
