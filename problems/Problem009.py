# -*- coding: utf-8 -*-
# Problem9.py>
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
# =============================================================================
# Starting with a = 1 and b = 499, we solve for c = sqrt(a^2 + b^2). If the 
# sum a + b + c = 1000 then we're done. Otherwise, we deprecate b, solve for c.
# and check the sum until a + b + c < 1000. At this point, we increase a by 1
# and repeat the process starting with b = (1000 - a) / 2.
# =============================================================================

import time

def main():
    start_time = time.time()
    
    a, b = 1, 499
    solved, failed = False, False
    
    while not solved and not failed:
        c = (a ** 2 + b ** 2) ** 0.5
        total = a + b + c
        if total == 1000:
            solved = True
        elif total > 1000:
            b -= 1
        else:
            a += 1
            b = int((1000 - a) / 2)
        if a >= 293:
            failed = True
    
    if failed:
        print("Oops! Didn't find a solution.")
    else:
        answer = int(a * b * c)
        total_time = time.time() - start_time
        print("Triple: {}, {}, {}.\nAnswer: {}.\nCalculation time: {}s."
              .format(a, b, int(c),answer, total_time))
    
if __name__ == "__main__":
    main()