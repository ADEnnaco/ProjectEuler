# -*- coding: utf-8 -*-
# Problem023.py>
"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
# =============================================================================
# We start off by finding all of the abundant numbers less than 28123. Next, we
# we find every possible sum of two abundant numbers using NumPy's meshgrid
# function. The answer is the sum of every number under 28123 that is not part
# of this list.
# =============================================================================

import numpy as np
from functions.integers import defperfabund

import time

def main():
    start_time = time.time()
    
    abundant = [m for m in range(12,28123) if defperfabund(m) == 'abundant']
    xx, yy = np.meshgrid(abundant, abundant)
    writeable = np.unique(xx + yy)
    non_writeable = np.setdiff1d(range(1,28123), writeable)
    answer = np.sum(non_writeable)    
    
    # Answer should be 4179871
    total_time = time.time() - start_time
    print("Answer: {}\nCalculation time: {:.3f}s".format(answer, total_time))
    
if __name__ == "__main__":
    main()