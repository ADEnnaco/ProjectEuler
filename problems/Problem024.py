# -*- coding: utf-8 -*-
# Problem024.py>
"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
# =============================================================================
# Thinking logically, the first 9! permutations will have 0 as the first digit.
# The next 9! will have 1, and so forth. This means if 999999 / 9! = q * n + r,
# q would tell us the first digit of the one millionth permutation, and r would
# tell uss how far into these permutations we'd find the one millionth overall.
# In other words, we want the rth permutation of the digits other than q. We
# can then simply repeat the above process.
# =============================================================================

from math import factorial

import time

def main():
    start_time = time.time()
    
    string = '0123456789'
    digits = len(string)
    n_perm = 999999
    answer = ""
    for i in range(digits-1,-1,-1):
        q, n_perm = divmod(n_perm, factorial(i))
        answer += string[q]
        string = string[:q] + string[q+1:]
    
    # Answer should be 2783915460
    total_time = time.time() - start_time
    print("Answer: {}\nCalculation time: {:.3f}s".format(answer, total_time))
    
if __name__ == "__main__":
    main()