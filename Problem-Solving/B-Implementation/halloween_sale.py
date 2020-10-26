#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    if s < p:
        return 0
    elif s == p or (s-p < p-d):
        return 1
    else:
        num_games = 0
        while p > m:
            if s > p:
                s -= p
                num_games += 1
                p -= d
        num_games += int(s/m)
        return(num_games)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
