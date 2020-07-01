
def print_formatted(number):
    max_length = len(bin(number)[2:])
    for x in range(1, number+1):
        print(str(x).rjust(max_length, ' '), end=' ') # decimal
        print(str(oct(x))[2:].rjust(max_length, ' '), end=' ') # octal
        print(str(hex(x))[2:].upper().rjust(max_length, ' '), end=' ') #hexadecimal
        print(str(bin(x))[2:].rjust(max_length, ' '), end='\n') # binary
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
