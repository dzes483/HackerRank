import re

regex = re.compile(r'''
                   ^(?=.*?\d{3,}))      # At least three digits
                   ((?=.*?[A-Z]{2,}))    # At least two uppercase letters
                   ((?=.*?[a-z]*))       # Any number of lowercase letters
                   ((?!.*\1\2\3))         # No repeating characters
                   [A-Za-z\d]{10}$       # 10 characters long
                    ''', re.VERBOSE)
for n in range(int(input())):
    match = re.fullmatch(regex, input())
    if match:
        print("Valid")
    else:
        print("Invalid")
 # ^(?=.*?[a-z]*[A-Z]{2,}))(?!.*\1\2)((?=.*?[0-9]{3,}))[A-Za-z0-9](?!.*\1)){{10}$
 ^(?=(?:[a-z\d]*[A-Z]){2})(?=(?:\D*\d){3})(?:([a-zA-Z\d])(?!.*\1)){10}$
