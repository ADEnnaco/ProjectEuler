# -*- coding: utf-8 -*-
# Problem027.py>
"""
Euler discovered the remarkable quadratic formula:

n^2+n+41

It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,40^2+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,41^2+41+41 is clearly divisible by 41.

The incredible formula n^2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n^2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
"""
# =============================================================================
# Since we need a prime value when n = 0, we determine that b must be a prime
# integer. Additionally, a must be odd otherwise the value will be even for
# even values of n. Furthermore, we can deduce through some algebraic
# manipulation that a needs to be greater than -(b/m + m) where m is the streak
# of primes that needs to be exceeded. The reason for this is that if a is less
# than this, the value of n^2 + an + b will become negative before n exceeds
# the streak maximum. With this in mind we iterate through the values of a and
# b looking for the optimum values.
# =============================================================================

from functions.integers import isprime
from functions.sequences import get_primes

import time

def main():
    start_time = time.time()
    
    limit = 1000
    most_primes = 40
    max_a, max_b = 0, 0
    primes = get_primes(limit)
    for b in primes[::-1]:
        if b < most_primes: continue
        m = -1 * int((b / most_primes) + most_primes)
        m = m if m & 1 == 1 else m + 1
        for a in range(m,limit,2):
            n = 1
            while isprime(n ** 2 + a * n + b):
                n += 1
            if n >= most_primes:
                most_primes = n
                max_a, max_b = a, b
    
    answer = max_a * max_b
    # Answer should be -59231
    total_time = time.time() - start_time
    print("a = {} b = {} primes = {}".format(max_a, max_b, most_primes))
    print("Answer: {}\nCalculation time: {:.3f}s".format(answer, total_time))
    
if __name__ == "__main__":
    main()