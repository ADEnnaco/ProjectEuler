# SumHelpers.py>
"""
Helper functions used to solve ProjectEuler problems.
"""

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
def sum_integers(n):
    """
    Calculates the sum of the first n integers.

    Parameters
    ----------
    n : integer
        The number of integers to sum.

    Returns
    -------
    sum: integer
        The sum of the first n integers, starting with 1

    """
    if isinstance(n, int):
        sum_ = int(n * (n + 1) / 2)
        return sum_
    else:
        print("ERROR: sum_integers received invalid input.")
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
def largest_multiple_less_than(base, limit):
    """
    Finds the largest multiple strictly less than the indicated limit.

    Parameters
    ----------
    base : integer
        The integer you want to find a multiple of.
    limit : integer or float
        The returned value is the largest multiple strictly less this value.

    Returns
    -------
    multiple: integer
        The largest multiple of 'base' that is strictly less than 'limit'.

    """
    if isinstance(base, int) and isinstance(limit, (int, float)):
        if limit % base == 0:
            multiple = int(limit - base)
        else: 
            multiple = int(limit - (limit % base))
        return multiple
    else:
        print("ERROR: largest_multiple_less_than received invalid input.")
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
    if isinstance(limit, (int, float)):
        multiple = largest_multiple_less_than(base, limit)
        count = int(multiple / base)
    if isinstance(count, int):
        sum_  = base * sum_integers(count)
        return sum_
    else:
        print("ERROR: sum_multiples received invalid input.")