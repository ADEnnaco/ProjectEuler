# -*- coding: utf-8 -*-
# integers.py>
"""
Functions related to the proprties of integers (e.g. factors and multiples).
"""
import numpy as np
from functions.sequences import get_primes
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
def prime_factorize(n):
    """
    Returns the unique prime factorization of an integer in the form of two 
    lists. The first list being the factors themselves, and the second their 
    respective multiplicites.

    Parameters
    ----------
    n : integer
        The number to be prime factorized.

    Returns
    -------
    factors : list of integers
        The prime factors of the integer in ascending order.
    multiplicities: list of integers.
        The corresponding multiplicities for each factor in the prime 
        factorization of the integer.
     
    Example
    -------    
    600 = (2^3)*(3^1)*(5^2)
    prime_factorize(600) returns
    factors = [2,3,5]
    multiplicities = [3,1,2]

    """
    if isinstance(n, int) and n > 1:
        # handles fringe cases of n = 2 or 3
        if n in [2, 3]:
            return [n], [1]
        
        # initialize factors and multiplicites
        factors = []
        multiplicities = []
        
        # generate list of potential prime factors
        primes = get_primes(n ** 0.5)
        
        # decompose n by dividing out primes
        for prime in primes:
            multiplicity = 0
            while n % prime == 0:
                n = int(n / prime)
                multiplicity += 1
            if multiplicity >= 1:
                factors.append(prime)
                multiplicities.append(multiplicity)
            if n == 1:
                break
        if n > 1:
            factors.append(n)
            multiplicities.append(1)
        return factors, multiplicities
    else:
        print("ERROR: prime_factorization received invalid input.\nREASON:",
              "n must be an integer greater than 1.")
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
def get_divisors(n):
    """
    Returns the positive integer divisors of an integer in ascending order.

    Parameters
    ----------
    n : integer
        The integer to find divisors of. Must be 2 or greater.

    Returns
    -------
    divisors : list of integers
        All divisors of an integer including 1 and the integer itself in 
        ascending order.

    """
    if isinstance(n, int) and n > 1:
        factors, multiplicities = prime_factorize(n)
        divisors = [1]
        for i in range(len(factors)):
            temp = [factors[i] ** x for x in range(multiplicities[i]+1)]
            divisors = [x * y for x in divisors for y in temp]
        divisors.sort()
        return divisors
    else:
        print("ERROR: get_divisors received invalid input.\nREASON: n must",
              "be an integer greater than 1.")
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
def num_divisors(n):
    """
    Returns the number of divisors n has, including 1 and n.

    Parameters
    ----------
    n : integer

    Returns
    -------
    num_divisors : integer
        The number of positive integer divisors of the number n.

    """
    if isinstance(n, int) and n > 0:
        if n == 1:
            return 1
        _, multiplicities = prime_factorize(n)
        num_divisors = np.prod([x + 1 for x in multiplicities])
        return num_divisors
    else:
        print("ERROR: num_divisors received invalid input.\nREASON: n must",
              "be a positive integer.")
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
def isprime(n):
    """
    Determines whether or not the input is prime.

    Parameters
    ----------
    n : integer
        

    Returns
    -------
    prime : bool
        True if n is a prime integer and False otherwise.

    """
    if isinstance(n, int) and n > 1:
        if n in [2,3]: return True
        for p in get_primes(n ** 0.5):
            if n % p == 0: return False
        return True
    else:
        return False
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
def lcm(a, b):
    """
    Returns the least common multiple of two positive integers.

    Parameters
    ----------
    a : integer
        One of the two integers.
    b : integer
        One of the two integers.

    Returns
    -------
    lcm : integer
        The least common multiple of a and b

    """
    if all(map(lambda x: isinstance(x, int), [a, b])):
        if a >= b:
            larger, smaller = a, b
        else:
            larger, smaller = b, a
        r = larger % smaller
        if r == 0:
            return larger
        r2 = smaller % r
        if r2 == 0:
            return int(larger * smaller / r)
        elif smaller % r2 == 0:
            return int(larger * smaller / r2)
        else:
            return larger * smaller
    else:
        print("ERROR: lcm received invalid input.\nREASON: a and b must be",
              "positive integers.")
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
        base = abs(base)
        if limit % base == 0:
            multiple = int(limit - base)
        else: 
            multiple = int(limit - (limit % base))
        return multiple
    else:
        print("ERROR: largest_multiple_less_than received invalid input.",
              "\nREASON: base must be an integer and limit must be numeric.")
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
def defperfabund(n):
    """
    Finds the sum of the proper divisors of an integer and returns whether the
    number is deficient, perfect, or abundant.

    Parameters
    ----------
    n : integer
        The integer to be classified.

    Returns
    -------
    num_type : string
        'deficient': sum of proper divisors < n
        'perfect': sum of proper divisors = n
        'abundant': sum of proper divisots > n

    """
    if isinstance(n, int) and n > 1:
        if n >= 12 and n % 6 == 0:
            return 'abundant'
        sum_divisors = sum(get_divisors(n)[:-1])
        if sum_divisors < n:
            return 'deficient'
        elif sum_divisors == n:
            return 'perfect'
        else:
            return 'abundant'
    else:
        print("ERROR: defperfabund received invalid input.\nREASON: n must be",
              "an integer greater than 1.")