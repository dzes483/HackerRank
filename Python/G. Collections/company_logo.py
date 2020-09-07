#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter



if __name__ == '__main__':
    count = Counter(list(input()))
    sorted_count = sorted(count.items(), key=lambda x: (-x[1], x[0]))
    for i, j in sorted_count[:3]:
        print(i, j)
