eng_n = int(input())
eng_nums = set([int(i) for i in (input().split())])
fra_n = int(input())
fra_nums = set([int(i) for i in (input().split())])

s = eng_nums.difference(fra_nums)

print(len(s))
