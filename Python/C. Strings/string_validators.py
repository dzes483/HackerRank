if __name__ == '__main__':
    s = input()
    args = ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper']
    for arg in args:
        print(any(getattr(char, arg)() for char in s))
