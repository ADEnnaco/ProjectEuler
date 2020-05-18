# -*- coding: utf-8 -*-
# Problem010.py>
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
# =============================================================================
# I've written a function that utilizes the Eratosthene Sieve algorithm to
# generate prime numbers. We use the function to generate all primes below
# 2,000,000 and then we sum the list.
# =============================================================================

from functions.sequences import get_primes

import time

def main():
    start_time = time.time()
    
    primes = get_primes(2e6)
    answer = sum(primes)
    
    total_time = time.time() - start_time
    print("The answer: {}.\nCalculation time: {}s.".format(answer, total_time))
    
if __name__ == "__main__":
    main()