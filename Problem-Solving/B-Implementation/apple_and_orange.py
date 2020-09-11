#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_on_house = 0
    oranges_on_house = 0
    for distance in apples:
        if a + distance in range(s, t+1):
            apples_on_house += 1
    for distance in oranges:
        if b + distance in range(s, t+1):
            oranges_on_house += 1
    print(apples_on_house)
    print(oranges_on_house)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
