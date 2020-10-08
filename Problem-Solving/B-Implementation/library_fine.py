#!/bin/python3

import math
import os
import random
import re
import sys
import datetime

# Complete the libraryFine function below.
def libraryFine(d1, m1, y1, d2, m2, y2):
    fmt = "%d %m %Y"
    returned_date = datetime.datetime.strptime(f'{d1} {m1} {y1}', fmt)
    due_date = datetime.datetime.strptime(f'{d2} {m2} {y2}', fmt)
    if returned_date <= due_date:
        fine = 0
    elif returned_date.year > due_date.year:
        fine = 10000
    elif returned_date > due_date and returned_date.month == due_date.month:
        overdue = returned_date - due_date
        fine = overdue.days*15
    elif returned_date > due_date and returned_date.year == due_date.year:
        overdue = returned_date.month - due_date.month
        fine = overdue*500
    return fine


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    d1M1Y1 = input().split()

    d1 = int(d1M1Y1[0])

    m1 = int(d1M1Y1[1])

    y1 = int(d1M1Y1[2])

    d2M2Y2 = input().split()

    d2 = int(d2M2Y2[0])

    m2 = int(d2M2Y2[1])

    y2 = int(d2M2Y2[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()
