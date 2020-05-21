# -*- coding: utf-8 -*-
# Problem015.py>
"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""
# =============================================================================
# For an m x n grid, the solution will always be (m + n)!/(m! * n!). However,
# for the sake of fun, the solution we implement is graphical.
#
# -|---|---|---|        -|---|---|---|        -|---|---|---|
#  |   |   |   |         |   |   |   |         |   |   | 1 |
# -|---|---|---|        -|---|---|---|        -|---|---|---|
#  |   |   |   |   ->    |   |   | 1 |   ->    |   | 2 | 1 |   ->
# -|---|---|---|        -|---|---|---|        -|---|---|---|
#  |   |   | 1 |         |   | 1 | 1 |         | 1 | 1 | 1 |
# -|---|---|---|        -|---|---|---|        -|---|---|---|
#
# =============================================================================

import numpy as np

import time

def main():
    start_time = time.time()
    
    m = 20
    n = 20
    array = np.ones((m + 1, n + 1))
    for i in range(1,m + 1):
        for j in range(1,n + 1):
            array[i][j] = array[i][j-1] + array[i-1][j]
    answer = int(array[m][n])
    
    # Answer should be 837799
    total_time = time.time() - start_time
    print("Answer: {}\nCalculation time: {:.3f}s".format(answer, total_time))
    
if __name__ == "__main__":
    main()