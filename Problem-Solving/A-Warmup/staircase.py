#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    chars = " #"
    for _ in range(n-1):
        print(chars.rjust(n))
        chars += "#"
    print(chars[1:].rjust(n))

if __name__ == '__main__':
    n = int(input())

    staircase(n)
