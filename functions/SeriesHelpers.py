# -*- coding: utf-8 -*-
# SeriesHelpers.py>
"""
Functions related to series used to solve ProjectEuler problems.
"""
import math
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
def get_fibonacci(n=1, limit=None):
    """
    Returns the nth number in the Fibonnaci series, or the largest Fibonacci
    number under an indicated value along with its position. If you enter 
    values for both parameters then n is ignored.

    Parameters
    ----------
    n : integer, optional
        The index of the Fibonnaci sequence to be returned where:
            F(1) = 1
            F(2) = 1
            F(n) = F(n-2) + F(n-1)
    limit: integer or float, optional
        The (exclusive) upper limit on the desired Fibonnaci number. If used
        then 'n' is ignored. The default is None.
    Returns
    -------
    Fn: integer
        The nth nummber in the Fibonacci sequence, or the largest Fibonacci 
        number strictly less than the given limit.
    n: integer (only if limit parameter is used)
        The position of Fn in the sequence.

    """
    phi = (1 + math.sqrt(5)) / 2
    psi = 1 - phi
    if limit != None:
        n = None
    if isinstance(limit, (int, float)):
        m = int(math.log(limit, phi)) + 1
        if get_fibonacci(m+1) > limit:
            return get_fibonacci(m), m
        else:
            return get_fibonacci(m+1), m+1
    if isinstance(n, int):
        Fn = (phi ** n - psi ** n) / math.sqrt(5)
        Fn = int(round(Fn,0))
        return Fn
    else:
        print("ERROR: get_fibonacci received invalid input.")
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
def get_primes(limit):
    """
    Generate a list of all prime numbers less than or equal to the given limit.
    The algorithm for Sieve of Eratosthenes  is implemented.

    Parameters
    ----------
    limit : integer or float
        The inclusive upper limit on primes to generate.

    Returns
    -------
    primes: list
        The prime numbers in ascending order less than or equal to 'limit'.

    """
    primes = []
    check = [True for x in range(limit)]
    check[0:1] = False, False
    i = 2
    while(i * i < limit):
      if check[i] == True:
        for j in range(2 * i, limit + 1, i):
          check[j] = False
      i += 1
    
    for i in range(limit + 1):
      if check[i]:
        primes.append(i)
        
    return primes