import re

regex_pattern = re.compile(r'^((M{0,3})?(CM|D|CD)?(C{0,3})?(XC|L|XL)?(X{0,3})?(IX|V|IV)?(I{0,3})?)$')



import re
print(str(bool(re.match(regex_pattern, input()))))
