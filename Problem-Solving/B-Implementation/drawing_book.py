#!/bin/python3

import os
import sys
from collections import deque

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    book = [i for i in range(1, n+1)]
    book_pages = deque([book[i:i + 2] for i in range(1, len(book), 2)])
    front = 1
    back = 0
    if p == 1:
        return 0
    else:
        while len(book_pages) != 1:
            if p not in book_pages[-1]:
                book_pages.pop()
                back += 1
            if p not in book_pages[0]:
                book_pages.popleft()
                front += 1
        return min(front, back)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
