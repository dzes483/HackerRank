
def mat_printer(i):
    if i%2 != 0:
        print((i*".|.").center(m, "-"))


if __name__ == '__main__':
    n, m = [int(x) for x in input().split()]
    for i in range(n):
        mat_printer(i)
    print("WELCOME".center(m, '-'))
    for i in reversed(range(n)):
        mat_printer(i)
