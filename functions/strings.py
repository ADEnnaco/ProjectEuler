# -*- coding: utf-8 -*-
# integers.py>
"""
Functions related to manipulating strings
"""

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
def ispalindrome(string):
    """
    Checks if a string is palindromic.

    Parameters
    ----------
    string : string
        You know what it is.

    Returns
    -------
    bool
        True if the string is a palindrome, and False otherwise.

    """
    if isinstance(string, (str, int, float)):
        string = str(string).replace(" ", "").lower()
        if len(string) in [0,1]:
            return True
        half_index = len(string) // 2
        first = string[:half_index]
        second = string[-half_index:]
        if first == second[::-1]:
            return True
        else:
            return False
    else:
        print("ERROR: ispalindrome received invalid input.\nREASON: input",
              "must be convertible to string format.")