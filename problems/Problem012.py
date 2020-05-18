# -*- coding: utf-8 -*-
# Problem012.py>
"""
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""
# =============================================================================
# We iterate through the triangle numbers finding the number of divisors, and
# return the first one that exceeds 500.
# =============================================================================

from functions.integers import num_divisors

import time

def main():
    start_time = time.time()
    
    Tn = 0
    count = 0
    solved = False
    while not solved:
        count += 1
        Tn += count
        if num_divisors(Tn) > 500:
            answer = Tn
            solved = True
            
    # Answer should be 76576500
    total_time = time.time() - start_time
    print("Answer: {}.\nCalculation time: {:.3f}s.".format(answer, total_time))
    
if __name__ == "__main__":
    main()