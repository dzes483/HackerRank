#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    shortest = min(arr)
    sticks = [len(arr)]
    while len(arr) > 0:
        arr = list(map(lambda x: x-shortest, arr))
        arr = [i for i in arr if i > 0]
        sticks.append(len(arr))
        try:
            shortest = min(arr)
        except ValueError:
            break
    return sticks[:-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
