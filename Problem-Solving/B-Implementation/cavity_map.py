#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(n, grid):
    if n == 1:
        return grid
    else:
        new_grid = [grid[0]]
        for row in range(1, n-1):
            new_row = []
            for number in range(n):
                if number == 0 or number == n-1:
                    new_row.append(grid[row][number])
                else:
                    if grid[row][number] > max(grid[row][number+1],
                    grid[row][number-1], grid[row+1][number], grid[row-1][number]):
                        new_row.append('X')
                    else:
                        new_row.append(grid[row][number])
            new_grid.append(''.join(new_row))
        new_grid.append(grid[-1])
        return new_grid



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
