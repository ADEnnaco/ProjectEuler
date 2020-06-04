# -*- coding: utf-8 -*-
# Problem037.py>
"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
# =============================================================================
# We start by forming all of the right-truncatable primes. We do this by taking
# the single digit primes and appending 1, 3, 7, and 9 to the end and checking
# which of the resulting 2-digit numbers are prime. We then repeat this on the
# 2-digit primes to find all 3-digit right-truncatable primes. This continues
# until no new primes are generated, at which point we have compiled all of the
# right-truncatable primes. Now, in order for a prime to be left-truncatable
# it needs to end in 2, 3, 5, or 7. However, the right-truncatable numbers all
# end in either 1, 3, 7, or 9, so we can filter down to the right-truncatable
# numbers that end in 3 or 7. Then we check each remaining prime to see if it
# is left_truncatable. 
# =============================================================================

from functions.integers import isprime

import time

def main():
    start_time = time.time()
    
    # generate all right-truncatable primes
    r_trunc = [[2,3,5,7]]
    while True:
        new = [10 * x + y for x in r_trunc[-1] for y in [1,3,7,9]]
        prime_new = [x for x in new if isprime(x)]
        if prime_new == []:
            break
        else:
            r_trunc.append(prime_new)
    r_trunc = [prime for sublist in r_trunc[1:] for prime in sublist]
    
    # filter out primes that don't end in 3 or 7
    r_trunc = [p for p in r_trunc if p % 10 in [3,7]]
    
    # check remaining primes for being left-truncatable
    lr_trunc = []
    for p in r_trunc:
        truncated = p
        while truncated > 9:
            truncated = int(str(truncated)[1:])
            if not isprime(truncated):
                break
        if truncated < 10:    
            lr_trunc.append(p)
        
    print(lr_trunc)
    answer = sum(lr_trunc)
    
    # Answer should be 748317
    total_time = time.time() - start_time
    print("Answer: {}\nCalculation time: {:.3f}s".format(answer, total_time))
    
if __name__ == "__main__":
    main()