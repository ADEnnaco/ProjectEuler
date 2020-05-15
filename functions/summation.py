# -*- coding: utf-8 -*-
# SumHelpers.py>
"""
Functions relating to the sums of sequences of numbers.
"""
from functions.integers import largest_multiple_less_than
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
def sum_integers(n_upper, n_lower=1):
    """
    Calculates the sum of the integers between an inclusive upper and lower 
    limit.

    Parameters
    ----------
    n_upper : integer
        The inclusive upper limit of the integers to be summed.
    n_lower : integer, optional (default is 1)
        The inclusive lower limit of the integers to be summed.
    Returns
    -------
    sum: integer
        The sum of the integers between n_upper and n_lower, inclusive.

    """
    if all(map(lambda x: isinstance(x, int), [n_upper, n_lower])):
        sum_ = int((n_upper + n_lower) * (n_upper - n_lower + 1) / 2)
        return sum_
    else:
        print("ERROR: sum_integers received invalid input.\nREASON: n_upper",
              "and n_lower must both be integers.")
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
def sum_multiples(base, count=1, limit=None):
    """
    Calculates the sum of the multiples of a base.

    Parameters
    ----------
    base : integer
        The integer you want to sum positive multiples of.
    count : integer, optional
        The quantity of multiples you'd like to sum. Will be overidden to None
        if a value is set for 'limit'. The default is 1.
    limit : integer or float, optional
        The (inclusive) upper limit of the multiples to sum. If used, then
        'count' is set to None. The default is None.

    Returns
    -------
    sum : integer
        The sum of the first 'count' multiples of the base.
        If 'limit' is set, then the sum of the multiples less than or equal to
        'limit' is returned instead.

    """
    if limit != None:
        count = None
    if isinstance(base, int) and isinstance(limit, (int, float)):
        multiple = largest_multiple_less_than(base, limit)
        count = int(multiple / base)
    if all(map(lambda x: isinstance(x, int), [base, count])):
        sum_  = base * sum_integers(count)
        return sum_
    else:
        print("ERROR: sum_multiples received invalid input.\nREASON: base and",
              "count must be integers, and limit must be numeric.")