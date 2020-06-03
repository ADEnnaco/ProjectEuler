# -*- coding: utf-8 -*-
# Problem034.py>
"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.
"""
# =============================================================================
# Similar to problem 30, we speed up our run time by examining combinations of
# digits rather than individual numbers. The primary difference here is that
# since we're using the factorial, and not the digit raised to a power, zeros
# have a contribution to the resulting total, so we adjust how we handle zeros
# accordingly.
# =============================================================================

from functions.combinatorics import digit_combos
from functions.conversions import sum_digit_factorial

import time

def main():
    start_time = time.time()
    
    numbers = []
    for combo in digit_combos(7):
        # reverse the string so zeros are at the end and are preserved
        # when convered to an integer
        combo = combo[::-1]
        # find sum of digit factorials
        total = sum_digit_factorial(int(combo))
        
        # handles errors caused by zeros in the middle of the total by removing
        # zeros one by one until the number and it's factorial digit total
        # have the same number of digits
        while len(combo) > len(str(total)) and combo[-1] == '0':
            combo = combo[:-1]
            total = sum_digit_factorial(int(combo))
        
        if list(combo[::-1]) == sorted(list(str(total))) and total > 9:
            numbers.append(total)
            
    print(numbers)
    answer = sum(numbers)
    # Answer should be 40730
    total_time = time.time() - start_time
    print("Answer: {}\nCalculation time: {:.3f}s".format(answer, total_time))
    
if __name__ == "__main__":
    main()