total_nums = int(input())
nums = [i for i in input().split()]

print(all(int(i)>0 for i in nums) and any(i == i[::-1] for i in nums))
