# -*- coding: utf-8 -*-
# combinatorics.py>
"""
Functions for combining and permuting.

"""
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