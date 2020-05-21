# -*- coding: utf-8 -*-
# Problem019.py>
"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
# =============================================================================
# I'm not reinventing the wheel on this one. We use Python's datetime module,
# iterate through the first of every month from 01/01/1901 through 12/31/2000,
# check the day of the week, and if it's Sunday, we increment the counter.
# =============================================================================

import datetime

import time

def main():
    start_time = time.time()
    
    answer = 0
    
    for year in range(1901,2001):
        for month in range(1,13):
            date = datetime.date(year, month, 1)
            if date.strftime("%A") == 'Sunday':
                answer += 1
    
    # Answer should be 171
    total_time = time.time() - start_time
    print("Answer: {}\nCalculation time: {:.3f}s".format(answer, total_time))
    
if __name__ == "__main__":
    main()