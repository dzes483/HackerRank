import re

regex_pattern = re.compile(r"#[A-F0-9]{3,6}", re.IGNORECASE)

for n in range(int(input())):
    code = input()
    if code.startswith('#'):
        pass
    else:
        for i in re.findall(regex_pattern, code):
            print(i)
