#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    if len(s) + len(t) < k:
        return "Yes"
    else:
        matches = 0
        for s_i, t_i in zip(s, t):
            if s_i == t_i:
                matches += 1
            else:
                break
        diff = (len(s) - matches) + (len(t) - matches)
        if diff <= k and diff % 2 == k %2:
            return "Yes"
        return "No"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
