# -*- coding: utf-8 -*-
# Problem014.py>
"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
# =============================================================================
# For each number from 2 to 999,999 we construct the collatz chain. When the 
# chain is completed, we store the length for every value in the chain. If, 
# while constructing the chain, we come across a value for which we already 
# know the chain length, we stop building and add the known chain length to 
# that of each value in the new chain.
# =============================================================================

from functions.sequences import collatz

import time

def main():
    start_time = time.time()
    
    # initialize problem parameters
    answer = 0
    max_num = 1000000
    max_chain = 0
    numbers = list(range(max_num))
    chain_length = [0 for x in range(max_num)]
    
    for num in numbers[2:]:
        # skip previously encountered numbers
        if num == 1: continue
        
        n = num
        chain = [n]
        done = False
        while not done:
            n = collatz(n)
            # force encountered numbers to be skipped later on
            if num < n < max_num:
                numbers[n] = 1
                
            chain.insert(0, n)
            if n < max_num and (chain_length[n] != 0 or n == 1):
                # every element in the chain has a chain length that is 1 more
                # than the element in front of it
                for i, x in enumerate(chain):
                    if x < max_num:
                        chain_length[x] = chain_length[n] + i
                done = True
                if chain_length[num] > max_chain:
                    max_chain = chain_length[num]
                    answer = chain[-1]
    
    # Answer should be 837799
    total_time = time.time() - start_time
    print("Answer: {}\nPath length: {}\nCalculation time: {:.3f}s"
          .format(answer, max_chain, total_time))
    
if __name__ == "__main__":
    main()