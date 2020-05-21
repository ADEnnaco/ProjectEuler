# -*- coding: utf-8 -*-
# Problem018.py>
"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

                                       3
                                      7 4
                                     2 4 6
                                    8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

                                      75
                                    95  64
                                  17  47  82
                                18  35  87  10
                              20  04  82  47  65
                            19  01  23  75  03  34
                          88  02  77  73  07  63  67
                        99  65  04  28  06  16  70  92
                      41  41  26  56  83  40  80  70  33
                    41  48  72  33  47  32  37  16  94  29
                  53  71  44  65  25  43  91  52  97  51  14
                70  11  33  28  77  73  17  78  39  68  17  57
              91  71  52  38  17  14  91  43  58  50  27  29  48
            63  66  04  68  89  53  67  30  73  16  69  87  40  31
          04  62  98  27  23  09  70  98  73  93  38  53  60  04  23
"""
# =============================================================================
# We find the highest scoring path by working backwards. Starting in the 2nd
# row from the bottom, for each number we find the highest scoring path that
# starts from that position. This is simply the number plus the higher of the
# two numbers we can move to in the row below. We then repeat this process,
# moving up the triangle row by row until we reach the top. After this is done,
# the maximum score will be whatever value is at the top of the triangle.
# =============================================================================

import numpy as np

import time
from bs4 import BeautifulSoup
import requests

def main():
    start_time = time.time()
    
    url = 'https://projecteuler.net/minimal=18'
    headers = {'user-agent': 'problem solver (andy.ennaco@gmail.com)'}
    response = requests.get(url, headers=headers)
    
    # make sure we got a valid response
    if(response.ok):
      # get the full data from the response
      data = response.text
    
    # parse html and store triangle as list of rows
    soup = BeautifulSoup(data, 'html.parser')
    triangle = soup.find_all('p')[4].get_text()
    rows_list = [row.split(' ') for row in triangle.split('\n')]
    
    # convert list to numpy array and full empty cells with zeroes
    tri_array = np.array([a + [0 for i in range(len(rows_list)-len(a))] \
                          for a in rows_list], dtype=int)
    
    # iterate through procedure detailed above
    rows, cols = tri_array.shape
    for i in range(rows - 2, -1, -1):
        for j in range(i + 1):
            tri_array[i][j] += max(tri_array[i+1][j], tri_array[i+1][j+1])
    
    answer = tri_array[0][0]
    
    # answer should be 1074
    total_time = time.time() - start_time
    print("Answer: {}\nCalculation time: {:.3f}s".format(answer, total_time))
    
if __name__ == "__main__":
    main()