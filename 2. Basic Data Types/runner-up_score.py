if __name__ == '__main__':
    n = int(input())
    new_set = set(map(int, input().split()))
    new_set.discard(max(new_set))
    print(max(new_set))
