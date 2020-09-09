#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    d = {'plus': 0, 'minus': 0, 'zero': 0}
    for n in arr:
        if n > 0:
            d['plus'] += 1
        elif n < 0:
            d['minus'] += 1
        elif n == 0:
            d['zero'] += 1
    for k, v in d.items():
        print(f"{v/len(arr):.6g}")

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
