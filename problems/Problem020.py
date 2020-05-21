# -*- coding: utf-8 -*-
# Problem020.py>
"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
# =============================================================================
# Starting at 2 (because 1 has no effect), and ending at 99 (since multiplying)
# by 100 doesn't affect digit sum), we multiply by all the integers. Every
# multiple of 5, we remove the trailing zeros in order to keep the number as
# small as possible without losing any information.
# =============================================================================

import time

def main():
    start_time = time.time()
    
    n_fact = 1
    for n in range(2,100):
        n_fact *= n
        if n % 5 == 0:
            n_fact = int(str(n_fact).strip('0'))
    
    answer = sum([int(digit) for digit in str(n_fact)])
    # Answer should be ***
    total_time = time.time() - start_time
    print("Answer: {}\nCalculation time: {:.3f}s".format(answer, total_time))
    
if __name__ == "__main__":
    main()