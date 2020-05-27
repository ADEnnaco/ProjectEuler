# -*- coding: utf-8 -*-
# Problem021.py>
"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
# =============================================================================
# We iterate through the numbers from 2 to 9,999 finding the sum of the proper
# divisors using the previously define get_divisors function. We then find the
# sum of the divisors of the new number, and see if it yields the original
# number. If so, the pair is added to the list of amicable pairs. Otherwise,
# we continue on. To prevent double counting (and save time), we skip any 
# number that is part of a discovered pair. Additionally, since one number from
# the pair must be higher than the other, we skip any number whose divisors sum
# to a smaller number than itself. A number whose proper divisors sum is less
# than itself is only part of an amicable pair if it's the larger number, which
# means we already would have found it when we checked the smaller of the two.
# =============================================================================

from functions.integers import get_divisors

import time

def main():
    start_time = time.time()
    
    amicable = []
    for u in range(2,10000):
        if u in amicable:
            continue
        v = sum(get_divisors(u)[:-1])
        if v <= u:
            continue
        w = sum(get_divisors(v)[:-1])
        if u == w:
            amicable += [u, v]
    
    print(amicable)
    answer = sum(amicable)
    # Answer should be 31626
    total_time = time.time() - start_time
    print("Answer: {}\nCalculation time: {:.3f}s".format(answer, total_time))
    
if __name__ == "__main__":
    main()