num_test_cases = int(input())

for case in range(num_test_cases):
    num_elems_a = int(input())
    set_a = set(int(i) for i in (input().split()))
    num_elems_b = int(input())
    set_b = set(int(i) for i in (input().split()))
    print(set_a.issubset(set_b))
