# -*- coding: utf-8 -*-
# Problem3.py>
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

"""
We find all of the prime numbers less than the square root of 600851475143.
Then we return the largest of these that is a factor.
"""
import time
start_time = time.time()

from math import sqrt
from functions.sequences import get_primes

answer = 600851475143
limit = int(sqrt(answer))
primes = get_primes(limit)
i = len(primes) - 1
while i >= 0:
    if answer % primes[i] == 0:
        answer = primes[i]
        break
    i -= 1

total_time = time.time()-start_time
print("The answer is {}.\nCalculation took {}ms.".format(answer, total_time))