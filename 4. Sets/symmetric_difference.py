M = int(input())
M_list = [int(i) for i in (input().split())] # convert the string input to int
N = int(input())
N_list = [int(i) for i in (input().split())] # convert the string input to int

# Get the symmetric distance
sym_dist_M = list(filter(lambda x: x in M_list and x not in N_list, M_list))
sym_dist_N = list(filter(lambda x: x in N_list and x not in M_list, N_list))

total = sym_dist_M + sym_dist_N
total = sorted(set(total))

for i in total:
    print(i)
