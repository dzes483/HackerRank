#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

# Complete the acmTeam function below.
def acmTeam(topic):
    max_team = 0
    max_topic = 0
    combos = combinations(topic,2)
    for i in combos:
        n = bin(((int(i[0],2) | int(i[1],2)))).count('1')
        if max_topic < n:
            max_topic = n
            max_team = 1
        elif n == max_topic:
            max_team +=1
    return max_topic, max_team

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
