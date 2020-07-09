from collections import Counter

num_shoes = int(input())
shoe_sizes = [int(i) for i in (input().split())]
num_customers = int(input())
profit = 0
counter = Counter(shoe_sizes)

for i in range(num_customers):
    size, price = [int(i) for i in (input().split())]
    if size in counter and counter[size] > 0:
        profit += price
        counter[size] -= 1
print(profit)
