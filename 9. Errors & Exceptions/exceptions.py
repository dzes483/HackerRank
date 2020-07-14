
num_test_cases = int(input())
for num in range(num_test_cases):
    a, b = input().split()
    try:
        print(int(a)//int(b))
    except (ZeroDivisionError, ValueError) as e:
        print(f"Error Code: {e}")
