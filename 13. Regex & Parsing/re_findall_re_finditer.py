import re

vowels = 'AEIOU'
consonants = 'QWRTYPSDFGHJKLZXCVBNM'

pattern = re.compile(rf"(?=[{consonants}]([{vowels}]{{2,}})[{consonants}])",
                   re.IGNORECASE)
matches = re.findall(pattern, input())

if matches == []:
    print(-1)
else:
    for i in matches:
        print(i)
