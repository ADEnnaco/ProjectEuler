# -*- coding: utf-8 -*-
# Problem032.py>
"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
"""
# =============================================================================
# We can show that the only possible situations are as follows:
#
#   (1-digit number) x (4-digit number) = (4-digit number)
#   (2-digit number) x (3-digit number) = (4-digit number)
#
# Therefore, we iterate through all the permutations of the digits 1 through 9
# partition them accordingly, and check to see of the product identity holds.
# =============================================================================

from functions.combinatorics import permutate

import time

def main():
    start_time = time.time()
    
    products = []
    for digits in permutate('123456789'):
        a, b, c = int(digits[:2]), int(digits[2:5]), int(digits[5:])
        m, n = int(digits[:1]), int(digits[1:5])
        if a * b == c and c not in products:
            print("{} x {} = {}".format(a,b,c))
            products.append(c)
        elif m * n == c and c not in products:
            print("{} x {} = {}".format(m,n,c))
            products.append(c)
    
    answer = sum(products)
    
    # answer should be 45228
    total_time = time.time() - start_time
    print("Answer: {}\nCalculation time: {:.3f}s".format(answer, total_time))

if __name__ == "__main__":
    main()