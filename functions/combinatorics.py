# -*- coding: utf-8 -*-
# combinatorics.py>
"""
Functions for combining and permuting.

"""
import numpy as np

def permutate(string):
    """
    Returns all of the unique permutations of the alphanumeric characters of a
    string.

    Parameters
    ----------
    string : string
        The string of characters to permute.

    Returns
    -------
    permutations : list of strings
        Every unique permutation of the characters of the input string. If the
        string is input in alphabetical order, then the output will also be 
        sorted alphabetically.

    """
    if isinstance(string, str):
        if len(string) == 1:
            return [string]
        else:
            permutations = []
            for i, ch in enumerate(string):
                # prevents duplicate permutations
                if string.index(ch) != i: continue
                
                substring = string[:i] + string[i+1:]
                permutations += [ch + subp for subp in permutate(substring)]
            return permutations
    else:
        print("ERROR: permutate received invalid input.\nREASON: input must",
              "be a string.")
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
def digit_combos(n, start=0, stop=9):
    """
    Returns all the possible unique combinations of digits of length n.
    
    Example: digit_combos(2) returns:
        ['00', '01', '11', '02', '12', '22', '03', '13', '23', '33', '04',
         '14', '24', '34', '44', '05', '15', '25', '35', '45', '55', '06',
         '16', '26', '36', '46', '56', '66', '07', '17', '27', '37', '47', 
         '57', '67', '77', '08', '18', '28', '38', '48', '58', '68', '78', 
         '88', '09', '19', '29', '39', '49', '59', '69', '79', '89', '99']

    Parameters
    ----------
    n : integer
        The number of digits in each combination.
    start : integer, optional (default = 0)
        The lowest digit to consider for each combination.
    stop : integer, optional (default = 9)
        The highest digit to consider for each combination.

    Returns
    -------
    combos : list of strings
        Each possible combination, as a string to preserve leading zeros.
        Combinations will all be given in ascending order.
    """
    if all(map(lambda x: isinstance(x, int), [n, start, stop])):
        if n == 1:
            return [str(x) for x in range(start, stop + 1)]
        else:
            combos = []
            for sub_combo in digit_combos(n-1, start, stop):
                for i in range(start, int(sub_combo[0])+1):
                    combos.append(str(i) + sub_combo)
            return combos
    else:
        print("ERROR: digit_combos received invalid input.\nREASON: n, start,",
              "and stop must all be integers.")
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
def monetary_combos(tot, denom):
    """
    Calculates the number of ways to make a given amount of money using the 
    denominations provided.

    Parameters
    ----------
    total : integer
        The amount of money to be represented in the lowest base unit.
    denominations : list of integers
        The denominations available to construct the total with.

    Returns
    -------
    combinations : integer
        The number of ways to make the indicated total using the denominations
        provided.

    """
    if all(map(lambda x: isinstance(x, int), [tot] + [y for y in denom])):
        combo_array = np.zeros((tot + 1, len(denom)), dtype=int)
        combo_array[0][0] = 1
        for amt in range(1, tot + 1):
            for i, coin in enumerate([x for x in denom if x <= tot]):
                combo_array[amt][i] = np.sum(combo_array[amt - coin][:i + 1])
                combinations = np.sum(combo_array[tot])
        return combinations
    else:
        print("ERROR: monetary_combos received invalid input.\nREASON: total",
              "and all denominations must be integers.")