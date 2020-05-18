# -*- coding: utf-8 -*-
# Problem6.py>
"""
The sum of the squares of the first ten natural numbers is:

1^2+2^2+...+10^2=385

The square of the sum of the first ten natural numbers is,:
    
(1+2+...+10)^2=55^2=3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
# =============================================================================
# The sum of the squares of the first n natural numbers is:
# 
#       (1/2)(n)(n+1)
# 
# The square of the sum of the first n natural numbers is:
#    
#       (1/6)(n)(n+1)(2n+1)
#
# Some algebraic manipulation shows a simplified form of the difference is:
# 
#       (1/12)(n-1)(n)(n+1)(3n+2)
# =============================================================================

import time

def main():
    start_time = time.time()
    
    n = 100
    answer = int((1 / 12) * (n - 1) * n * (n + 1) * (3*n + 2))
    
    total_time = time.time() - start_time
    print("The answer is {}.\nCalculation took {}s.".format(answer,
                                                            total_time))
    
if __name__ == "__main__":
    main()