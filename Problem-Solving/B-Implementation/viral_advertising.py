#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    likes = 2
    shares = 5
    total_likes = 2
    if n == 1:
        return likes
    else:
        for _ in range(2, n+1):
            shares = likes*3
            likes = shares//2
            total_likes += likes
        return total_likes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
