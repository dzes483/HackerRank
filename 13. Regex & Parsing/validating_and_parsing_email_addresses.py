import re

regex_pattern = re.compile(r"^[A-Z][A-Z0-9-._]+@[A-Z]+\.[A-Z]{1,3}", re.IGNORECASE)

for i in range(int(input())):
    name, email = input().split()
    if re.fullmatch(regex_pattern, email[1:-1]):
        print(name, email)
