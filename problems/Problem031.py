# -*- coding: utf-8 -*-
# Problem031.py>
"""
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""
# =============================================================================
# We solve this one from the bottom up. The algorithm implemented in
# monetary_combos starts off by making smaller amounts. We consider removing
# coins from the total one at a time, with each successive coin being either
# equal to, or smaller in value than the one prior. Each specific value can be
# be made a number of times equal to the sum of the ways to make the amounts
# yielded when removing a single coin value.
# =============================================================================

from functions.combinatorics import monetary_combos

import time

def main():
    start_time = time.time()
    
    total = 200
    denominations = [1, 2, 5, 10, 20, 50, 100, 200]
    answer = monetary_combos(total, denominations)
    
    # Answer should be 73682
    total_time = time.time() - start_time
    print("Answer: {}\nCalculation time: {:.3f}s".format(answer, total_time))
    
if __name__ == "__main__":
    main()