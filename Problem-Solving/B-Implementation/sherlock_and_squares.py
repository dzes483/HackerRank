#!/bin/python3

import math
import os
import random
import re
import sys
from math import sqrt
from array import array
import math

# Complete the squares function below.
def squares(a, b):
    a_sqrt = math.ceil(sqrt(a))
    print(a_sqrt)
    b_sqrt = math.floor(sqrt(b))
    print(b_sqrt)
    return (b_sqrt - a_sqrt) + 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
