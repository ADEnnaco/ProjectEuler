# -*- coding: utf-8 -*-
# Problem035.py>
"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
# =============================================================================
# With the exception of the numbers 2 and 5, a circular prime must be comprised
# entirely of the digits 1, 3, 7, or 9. This is because any other digit at the
# end of a number will result in it being composite. We create a list of prime
# numbers and then narrow it down to the ones that are made up of these digits.
# Then we iterate through them checking their rotations for prime-ness
# =============================================================================

from functions.sequences import get_primes

import time

def main():
    start_time = time.time()
    
    # initialize lists for storing circular and non-circular primes
    circular = []
    non_circular = []
    
    primes = get_primes(1000000)
    digits = {'1', '3', '7', '9'}
    
    # create list of potential circular prime numbers
    potential = ['2', '5'] 
    potential += [str(p) for p in primes if set(str(p)).issubset(digits)]
    # print(len(potential))
    for p in potential:
        if int(p) in circular + non_circular: continue
        rotations = []
        for i in range(len(p)):
            rotations.append(int(p[i:] + p[:i]))
            if str(rotations[i]) not in potential:
                non_circular += rotations
                rotations = []
                break
        circular += rotations
    
    circular = sorted(set(circular))
    print(circular)
    answer = len(circular)
    
    # Answer should be 55
    total_time = time.time() - start_time
    print("Answer: {}\nCalculation time: {:.3f}s".format(answer, total_time))
    
if __name__ == "__main__":
    main()