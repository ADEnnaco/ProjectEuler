# -*- coding: utf-8 -*-
# Problem017.py>
"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""
# =============================================================================
# I've written a function that will convert any number less than or equal to
# 1000 into text. We iterate through the digits, making the conversion and 
# stripping away spaces and hyphens, keeping a running character total along
# the way.
# =============================================================================

from functions.conversions import num2text

import time

def main():
    start_time = time.time()
    
    answer  = 0
    for n in range(1001):
        n_string = num2text(n).replace(" ","").replace("-","")
        n_length = len(n_string)
        answer += n_length
    
    # Answer should be 21124
    total_time = time.time() - start_time
    print("Answer: {}\nCalculation time: {:.3f}s".format(answer, total_time))
    
if __name__ == "__main__":
    main()