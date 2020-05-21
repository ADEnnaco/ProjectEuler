# -*- coding: utf-8 -*-
# Problem016.py>
"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""
# =============================================================================
# We calculate 2^1000, convert it to a list of digits, then add the digits.
# =============================================================================

import time

def main():
    start_time = time.time()
    
    num = 2 ** 1000
    digits = list(str(num))
    answer = sum([int(digit) for digit in digits])
    
    # Answer should be 1366
    total_time = time.time() - start_time
    print("Answer: {}\nCalculation time: {:.3f}s".format(answer, total_time))
    
if __name__ == "__main__":
    main()