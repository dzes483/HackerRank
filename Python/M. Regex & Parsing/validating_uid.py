import re

regex = re.compile(r'''
                   ^                          # Start of line
                   (?=(?:[a-z\d]*[A-Z]){2})   # At least two uppercase letters
                   (?=(?:\D*\d){3})           # At least three digits
                   (?:([a-zA-Z\d])            # Only alphanumeric characters
                   (?!.*\1))                  # No repeating characters
                   {10}                       # Length of 10
                   $                          # End of line
                    ''', re.VERBOSE)
for n in range(int(input())):
    match = re.fullmatch(regex, input())
    if match:
        print("Valid")
    else:
        print("Invalid")
