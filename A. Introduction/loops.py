if __name__ == '__main__':
    while True:
        n = int(input())
        if n in range(1, 21):
            break
        else:
            print('Please enter a number between 1 and 20.')
            continue

    for i in range(0, n):
        print(i*i)
