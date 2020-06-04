# -*- coding: utf-8 -*-
# Problem036.py>
"""
The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
# =============================================================================
# We start by constructing all of the palindromic numbers less than 1 million.
# This can be done taking all the numbers less than 1,000 and appending their
# reverse to the end with either nothing or a single digit in between. Then we
# check each for palindromic property in base 2.
# =============================================================================

from functions.strings import ispalindrome

import time

def main():
    start_time = time.time()
    
    mid = ['','0','1','2','3','4','5','6','7','8','9']
    # 1-digit palindromes
    pal = ['1','2','3','4','5','6','7','8','9']
    # 2, 3, 4 and 5-digit palindromes
    pal += [str(x) + y + str(x)[::-1] for x in range(1,100) for y in mid]
    # 6-digit palindromes
    pal += [str(x) + str(x)[::-1] for x in range(100,1000)]
    
    pal = [int(x) for x in pal]
    # filters for palindromes that are palindromic in base 2
    dec_bin_pal = [x for x in pal if ispalindrome(bin(x).replace("0b", ""))]
    
    print(sorted(dec_bin_pal))
    answer = sum(dec_bin_pal)
    
    # Answer should be 872187
    total_time = time.time() - start_time
    print("Answer: {}\nCalculation time: {:.3f}s".format(answer, total_time))
    
if __name__ == "__main__":
    main()