# -*- coding: utf-8 -*-
# Problem030.py>
"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
# =============================================================================
# We can reason that since 9^5 is 59,049, it's impossible for any number longer
# than 6 digits to have the desired property. Additionally, we substantially
# speed up our search time by considering combinations of digits rather than
# individual numbers. For example, it doesn't make sense to check both 312,995
# and 295,139 since they have the same digits. By taking advantage of this, we
# drastically reduce run time, and make the solution scale much better,
# =============================================================================

from functions.combinatorics import digit_combos
from functions.conversions import sum_digit_power

import time

def main():
    start_time = time.time()
    
    numbers = []
    for combo in digit_combos(6):
        total = sum_digit_power(int(combo), 5)
        
        # handles errors caused by zeros in the middle of the total
        while len(combo) > len(str(total)) and combo[0] == '0':
            combo = combo[1:]
        
        if list(combo) == sorted(list(str(total))) and total > 1:
            numbers.append(total)
            
    print(numbers)
    answer = sum(numbers)
    # Answer should be 443839
    total_time = time.time() - start_time
    print("Answer: {}\nCalculation time: {:.3f}s".format(answer, total_time))
    
if __name__ == "__main__":
    main()