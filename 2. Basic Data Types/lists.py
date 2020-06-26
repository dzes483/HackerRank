if __name__ == '__main__':
    my_list = []
    for i in range(int(input())):
        args = input().split()
        if args[0] == 'print':
            print(my_list)
        elif len(args) == 3: # for the insert function
            getattr(my_list, args[0])(int(args[1]), int(args[2]))
        elif len(args) == 2: # for remove and append
            getattr(my_list, args[0])(int(args[1]))
        elif len(args) == 1: # for pop, sort, and reverse
            getattr(my_list, args[0])()
