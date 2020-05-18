# -*- coding: utf-8 -*-
# Problem7.py>
"""
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
"""
# =============================================================================
# We treat the number as a string. Since any product including the digit 0 will
# automatically be zero, we split the string with 0 as a delimiter. Then we go
# through each substring calculating 13-digit products, ignoring any strings
# that are less than 13 digits long.
# =============================================================================

import time
from bs4 import BeautifulSoup
import requests

def main():
    start_time = time.time()
    
    # initialize variables
    answer = 0
    length = 13

    url = 'https://projecteuler.net/problem=8'
    response = requests.get(url)
    
    # make sure we got a valid response
    if(response.ok):
      # get the full data from the response
      data = response.text
    
    # parse html and store 1000-digit number
    soup = BeautifulSoup(data, 'html.parser')
    num = soup.find_all('p')[1].get_text().replace('\n', '')
    
    # split digits at zeroes
    substrings = num.split('0')
    
    # If a substring is at least 13 digits, we calculate the product of the
    # first 13 digits, compare it to the current answer, replacing if longer.
    # Then we crawl along substring one digit at a time, multiplying by the 
    # new digit and dividing by the removed one. This is repeated for each 
    # substring.
    for substring in substrings:
        if len(substring) >= length:
            substring = list(map(int, substring))
            product = 1
            for x in substring[:length]:
                product = product * x
            if product > answer: answer = product
            for i, x in enumerate(substring[length:]):
                product = int(product * x / substring[i])
                if product > answer: answer = product
    
    # Answer should be 23514624000
    total_time = time.time() - start_time
    print("The answer is {}.\nCalculation took {}s.".format(answer,
                                                            total_time))
    
if __name__ == "__main__":
    main()