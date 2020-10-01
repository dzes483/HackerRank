#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    z = list(zip(c, list(range(0,len(c)))))
    energy = 100
    start = 0
    loop = True
    while loop:
        for i in z[start::k]:
            energy -= 1
            if i[0] == 1:
                energy -= 2
            if i[1] + k == len(c):
                loop = False
            elif i[1] + k > len(c):
                start = (i[1] + k) - len(c)
                continue
            else:
                continue
    return energy

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
