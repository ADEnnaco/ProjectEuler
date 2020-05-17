# -*- coding: utf-8 -*-
# Problem7.py>
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
# =============================================================================
# I've written a function that utilizes the Eratosthene Sieve algorithm to
# generate prime numbers. We use the function to generate the first 10,001
# prime numbers, then return the last entry.
# =============================================================================

from functions.sequences import get_nprimes

import time

def main():
    start_time = time.time()
    
    answer = get_nprimes(10001)[-1]
    
    total_time = time.time() - start_time
    print("The answer is {}.\nCalculation took {}s.".format(answer,
                                                            total_time))
    
if __name__ == "__main__":
    main()