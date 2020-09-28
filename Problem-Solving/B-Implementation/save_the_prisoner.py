#!/bin/python3

import math
import os
import random
import re
import sys
from collections import OrderedDict

# Complete the saveThePrisoner function below.
def saveThePrisoner(prisoners, sweets, chair):
    if (sweets + chair -1) <= prisoners:
        return sweets + chair-1
    else:
        if (chair + sweets -1)%prisoners == 0:
            return prisoners
        else:
            return (chair+sweets-1)%prisoners


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
