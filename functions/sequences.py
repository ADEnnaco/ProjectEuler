# -*- coding: utf-8 -*-
# sequences.py>
"""
Functions relating to generating sequences of numbers.
"""
import math
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
        The prime numbers, in ascending order, less than or equal to 'limit'.

    """
    if isinstance(limit, (int, float)) and limit >= 2:
        limit = int(limit)
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
    else:
        print("ERROR: get_primes received invalid input.\nREASON: limit must",
              "be numeric and no less than 2.")
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
def get_nprimes(n):
    """
    Generate a list of the first n prime numbers. The algorithm for Sieve of 
    Eratosthenes  is implemented using an upper limit of:
        n * (ln(n) + ln(ln(n)))
    for any n >= 5.

    Parameters
    ----------
    n : integer
        The number of primes to return.

    Returns
    -------
    primes: list of integers
        The first n prime numbers, in ascending order.

    """
    if isinstance(n, int) and n > 0:
        if n >= 6:
            limit = n * (math.log(n) + math.log(math.log(n)))
            primes = get_primes(limit)[:n]
            return primes
        elif n == 5:
            return [2, 3, 5, 7, 11]
        elif n == 4:
            return [2, 3, 5, 7]
        elif n == 3:
            return [2, 3, 5]
        elif n == 2:
            return [2, 3]
        elif n == 1:
            return [2]
    else:
        print("ERROR: get_nprimes received invalid input.\nREASON: n must be",
              "a positive integer.")
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
def get_fibonacci(n=1, limit=None):
    """
    Returns the nth number in the Fibonnaci series, or the largest Fibonacci
    number under an indicated value along with its position. If you enter values
    for both parameters then n is ignored.

    Parameters
    ----------
    n : integer, optional (default = 1)
        The index of the Fibonnaci sequence to be returned where:
            F(1) = 1
            F(2) = 1
            F(n) = F(n-2) + F(n-1)
    limit: integer or float, optional (default = None)
        The (exclusive) upper limit on the desired Fibonnaci number. If used
        then 'n' is ignored.
    Returns
    -------
    Fn: integer
        The nth nummber in the Fibonacci sequence, or the largest Fibonacci 
        number strictly less than the given limit.
    n: integer (only if limit parameter is used)
        The position of Fn in the sequence.

    """
    phi = (1 + 5 ** 0.5) / 2
    psi = 1 - phi
    if limit != None:
        n = None
    if isinstance(limit, (int, float)) and limit > 0:
        m = int(math.log(limit, phi)) + 1
        if get_fibonacci(m + 1) > limit:
            return get_fibonacci(m), m
        else:
            return get_fibonacci(m + 1), m + 1
    if isinstance(n, int) and n > 0:
        """
             (phi)^n - (1-phi)^n              sqrt(5) + 1
        Fn = -------------------  , where phi = -----------
                  sqrt(5)                          2
        """
        Fn = (phi ** n - psi ** n) / math.sqrt(5)
        Fn = int(round(Fn,0))
        return Fn
    else:
        print("ERROR: get_fibonacci received invalid input.\nReason: limit",
              "must be a positive number or n must be a positive integer.")
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------