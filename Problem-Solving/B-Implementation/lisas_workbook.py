#!/bin/python3

import math
import os
import random
import re
import sys
from math import ceil
import itertools

# n = num_chapters
# k = max number of problems per page
# arr = number of problems in each chapter

# Complete the workbook function below.
def workbook(n, k, arr):
    special_probs = 0
    page_num = 0
    for ch in arr:
        page_num += 1
        for problem in range(1, ch+1):
            if problem == page_num:
                special_probs += 1
            if problem%k == 0 and problem < ch:
                page_num += 1
    return special_probs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
