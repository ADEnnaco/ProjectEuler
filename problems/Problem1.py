# Problem1.py>
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
import time
start_time = time.time()
from functions.SumHelpers import sum_multiples

# S(3 or 5) = S(3) + S(5) - S(3 and 5)
# where S(3 and 5) = S(15)
sum3 = sum_multiples(3, limit=1000)
sum5 = sum_multiples(5, limit=1000)
sum15 = sum_multiples(15, limit=1000)
answer = sum3 + sum5 - sum15

total_time = time.time()-start_time
print("The answer is {}.\nCalculation took {}ms.".format(answer, total_time))