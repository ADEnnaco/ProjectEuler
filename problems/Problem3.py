# -*- coding: utf-8 -*-
# Problem3.py>
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""
import time

def main():
    start_time = time.time()
    
    num = 600851475143
    answer = 2
    
    # remove all factors of 2
    while num&1 == 0:
        num = num / 2
    
    # check if number was a power of 2
    if num == 1:
        total_time = time.time()-start_time
        print("The answer is {}.\nCalculation took {}s.".format(answer,
                                                                 total_time))
    
    # remove higher prime factors
    i = 3
    while i * i <= num:
        while num % i == 0:
            answer = i
            num = num / i
        i += 2
    
    # checks for fringe case of num = 5 or 7    
    if num > answer:
        answer = int(num)
    
    total_time = time.time()-start_time
    print("The answer is {}.\nCalculation took {}s.".format(answer,
                                                             total_time))

if __name__ == "__main__":
    main()