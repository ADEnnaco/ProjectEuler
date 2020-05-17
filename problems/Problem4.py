# -*- coding: utf-8 -*-
# Problem4.py>
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
# =============================================================================
# The largest number that is the product of two 3-digit numbers is 999^2 which
# is 998,001. Therefore, the largest possible answer is 997,799. Starting here,
# we generate each palindrome p, find the divisors, see if there exists a
# divisor d such that sqrt(p) < d < 1000. If this divisor exists, and p is a 
# 6-digit number then p / d will also be 3-digits, and we have our solution.
# =============================================================================

from functions.integers import get_divisors

import time

def main():
    start_time = time.time()
    first = 997
    answer = None
    while first >= 100:
        second = int(str(first)[::-1])
        p = 1000 * first + second
        divisors = get_divisors(p)
        for divisor in divisors:
            if divisor < p ** 0.5:
                continue
            if divisor >= 1000:
                break
            answer = p
        if answer:
            total_time = time.time() - start_time
            print("The answer is {}.\nCalculation took {}s.".format(answer,
                                                             total_time))
            return
        first -= 1
    print("Didn't find a 6-digit solution.")

if __name__ == "__main__":
    main()        