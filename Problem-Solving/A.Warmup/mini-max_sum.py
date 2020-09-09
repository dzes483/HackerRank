#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sums = []
    combos = itertools.combinations(arr, 4)
    for i in combos:
        sums.append(sum(i))
    print(min(sums), max(sums))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
