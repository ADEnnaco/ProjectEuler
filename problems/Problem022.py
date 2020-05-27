# -*- coding: utf-8 -*-
# Problem022.py>
"""
Using names.txt, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
# =============================================================================
# We import the read the file and convert it to a list. After using Python's
# list.sort() method we iterate through the enumerated list, calculating the 
# value of each name and finding the product of that value and its position in
# the list.
# =============================================================================

from functions.conversions import string2score

import time

def main():
    start_time = time.time()
    
    answer = 0
    
    f = open("../text_files/names.txt", "r")
    names = f.read().replace('"', '').split(",")
    names.sort()
    for i, name in enumerate(names, start=1):
        answer += i * string2score(name)
    
    # Answer should be 871198282
    total_time = time.time() - start_time
    print("Answer: {}\nCalculation time: {:.3f}s".format(answer, total_time))
    
if __name__ == "__main__":
    main()