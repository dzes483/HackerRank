#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the minimumDistances function below.
def minimumDistances(a):
    counts = Counter(a)
    distances = []
    for i in a:
        if counts[i] > 1:
            index_1 = a.index(i)
            diff = (a.index(i, index_1+1)) - index_1
            if diff > 0:
                distances.append(diff)
    return (min(distances) if distances else -1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
