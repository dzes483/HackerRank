cube = lambda x: x**3

def fibonacci(n):
    result = [0, 1]
    if n == 0:
        return []
    elif n == 1:
        return [0]
    else:
        for i in range(2, n):
            result.append(result[i-1] + result[i-2])
        return result

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
