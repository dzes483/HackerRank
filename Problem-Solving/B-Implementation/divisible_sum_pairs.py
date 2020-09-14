#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    num_pairs = 0
    for i, j in itertools.combinations(ar, 2):
        if (i + j) % k == 0:
            num_pairs += 1
    return num_pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
