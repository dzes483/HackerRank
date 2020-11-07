#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(N, B):
    if len(B) <= 2 or sum(B)%2 != 0:
        return "NO"
    else:
        count = 0
        for i in range(len(B)):
            if B[i]%2 != 0:
                count += 2
                B[i+1] += 1
        return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(N, B)

    fptr.write(str(result) + '\n')

    fptr.close()
