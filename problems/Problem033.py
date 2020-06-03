# -*- coding: utf-8 -*-
# Problem033.py>
"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""
# =============================================================================
# The numerator and denominator both need to be 2-digits, with a single shared
# digit between them. We can reason that neither number can include a zero, and
# that the 2 digits must be distinct. We narrow down our search to just these
# numbers, then we iterate through the numbers as possible numberators, pairing
# them with each other number that shares a digit and is larger in magnitude,
# since the fraction must be smaller than 1.
# =============================================================================

from fractions import Fraction

import time

def main():
    start_time = time.time()
    
    product = Fraction(1,1)
    fractions = []
    nums = [x for x in range(12,100) if x % 10 != 0 and x % 11 != 0]
    for num in nums:
        dens = [x for x in nums if int(x / 10) == num % 10 and x > num]
        for den in dens:
            if num * (den % 10) == den * int(num / 10):
                fractions.append("{}/{}".format(num,den))
                product *= Fraction(num, den)
        dens = [x for x in nums if int(num / 10) == x % 10 and x > num]
        for den in dens:
            if num * int(den / 10) == den * (num % 10):
                fractions.append("{}/{}".format(num,den))
                product *= Fraction(num, den)
    
    answer = product.denominator
    
    # answer should be 100
    total_time = time.time() - start_time
    print(fractions)
    print("Answer: {}\nCalculation time: {:.3f}s".format(answer, total_time))

if __name__ == "__main__":
    main()