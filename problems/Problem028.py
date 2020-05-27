# -*- coding: utf-8 -*-
# Problem028.py>
"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""
# =============================================================================
# The top right of each corner is s^2, with s the side length of the square.
# Excluding the center, the sum of the four corners can be shown to be:
# 
#                           4s^2 - 6s + 6.
# 
# Summing this over the odd values of s from 3 to n we get:
#
#                    (4n^3 + 3n^2 + 8n - 15) / 6
# 
# All that remains is to add back in the 1 in the center leaving us with a
# total along both diagonals for a spiral of side length n equal to:
# 
#                    (4n^3 + 3n^2 + 8n - 9) / 6
# 
# =============================================================================

import time

def main():
    start_time = time.time()
    
    n = 1001
    answer = int((4 * n ** 3 + 3 * n ** 2 + 8 * n - 9) / 6)
    
    # Answer should be 669171001
    total_time = time.time() - start_time
    print("Answer: {}\nCalculation time: {:.3f}s".format(answer, total_time))
    
if __name__ == "__main__":
    main()