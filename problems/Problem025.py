# -*- coding: utf-8 -*-
# Problem025.py>
"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""
# =============================================================================
# The nth Fibonacci number is given by
#
#             (phi)^n - (1-phi)^n              sqrt(5) + 1
#        Fn = -------------------  , where phi = -----------
#                  sqrt(5)                          2
#
# In general, the smallest integer strictly greater than log(N) will tell us
# how many digits N has. Putting these together, along with the notion that for
# for large n, (phi)^n >> (1-phi)^n, we can deduce that the index of the first
# Fibonacci number with 1000 digits will be the smallest integer greater than
# (999 + 0.5 * log(5)) / log(phi)
# =============================================================================

from math import log10

import time

def main():
    start_time = time.time()
    
    digits = 1000
    phi = (1 + 5 ** 0.5) / 2
    answer = int((digits - 1 + 0.5 * log10(5)) / log10(phi)) + 1
    
    # Answer should be 4782
    total_time = time.time() - start_time
    print("Answer: {}\nCalculation time: {:.3f}s".format(answer, total_time))
    
if __name__ == "__main__":
    main()