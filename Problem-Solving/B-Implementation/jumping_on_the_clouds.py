#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    while len(c) > 1:
        try:
            if len(c) >= 3 and c[2] == 0:
                jumps += 1
                del c[:2]
            elif len(c) >= 2 and c[1] == 0:
                jumps += 1
                del c[:1]
        except IndexError:
            continue
    return jumps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
