# -*- coding: utf-8 -*-
# Problem026.py>
"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	 = 	0.5
1/3	 = 	0.(3)
1/4	 = 	0.25
1/5	 = 	0.2
1/6	 = 	0.1(6)
1/7	 = 	0.(142857)
1/8	 = 	0.125
1/9	 = 	0.(1)
1/10 = 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""
# =============================================================================
# A fraction of the form 1/d will have, for its repeating cycle, at most p - 1
# digits, where p is its largest prime factor. For this reason, we only need to
# prime value for d. From here, we note that the length of the repeating cycle
# will be the same as the number of iterations (10 * r) mod d takes to repeat.
# =============================================================================

from functions.sequences import get_primes

import time

def main():
    start_time = time.time()
    
    answer, max_cycle = 0, 0
    for d in get_primes(1000)[3:]:
        cycle, r = 0, 1
        while r != 1 or cycle == 0:
            r = (10 * r) % d
            cycle += 1
        if cycle > max_cycle:
            answer, max_cycle = d, cycle
    
    # Answer should be 983
    total_time = time.time() - start_time
    print("Answer: {}\nCalculation time: {:.3f}s".format(answer, total_time))
    
if __name__ == "__main__":
    main()