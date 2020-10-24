#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    kaprekar_nums = [1, 9, 45, 55, 99, 297, 703, 999, 2223, 2728, 4950, 5050,
                     7272, 7777, 9999, 17344, 22222, 77778, 82656, 95121, 99999]
    results = []
    for num in kaprekar_nums:
        if num in range(p, q+1):
            results.append(num)
    if results:
        print(*results)
    else:
        print('INVALID RANGE')

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
