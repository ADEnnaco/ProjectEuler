# -*- coding: utf-8 -*-
# Problem5.py>
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
# =============================================================================
# Starting with 2520, we iterate from 11 up to 20, finding the least common
# multuple each time.
# =============================================================================

from functions.integers import lcm

import time

def main():
    start_time = time.time()
    
    answer = 2520
    for i in range(11,21):
        answer = lcm(answer, i)
    
    total_time = time.time() - start_time
    print("The answer is {}.\nCalculation took {}s.".format(answer,
                                                            total_time))
    
if __name__ == "__main__":
    main()