# -*- coding: utf-8 -*-
# conversions.py>
"""
Functions for converting between different units or data types

"""
from math import factorial

def num2text(number):
    """
    Converts a positive integer less than or equal to 1000 into text.

    Parameters
    ----------
    number : integer
        The number to convert.

    Returns
    -------
    number_as_text : string
        The number in English text.

    """
    if isinstance(number, int) and 0 < number <= 1000:
        a = str(number).zfill(4)
        
        unit = {'0': "",
                 '1': "one",
                 '2': "two",
                 '3': "three",
                 '4': "four",
                 '5': "five",
                 '6': "six",
                 '7': "seven",
                 '8': "eight",
                 '9': "nine"}
        
        teen = {'0': "ten",
                 '1': "eleven",
                 '2': "twelve",
                 '3': "thirteen",
                 '4': "fourteen",
                 '5': "fifteen",
                 '6': "sixteen",
                 '7': "seventeen",
                 '8': "eighteen",
                 '9': "nineteen"}
        
        hyph = {'0': ""}
        
        tens = {'0': unit[a[3]],
                '1': teen[a[3]],
                '2': "twenty" + hyph.get(a[3], "-") + unit[a[3]],
                '3': "thirty" + hyph.get(a[3], "-") + unit[a[3]],
                '4': "forty" + hyph.get(a[3], "-") + unit[a[3]],
                '5': "fifty" + hyph.get(a[3], "-") + unit[a[3]],
                '6': "sixty" + hyph.get(a[3], "-") + unit[a[3]],
                '7': "seventy" + hyph.get(a[3], "-") + unit[a[3]],
                '8': "eighty" + hyph.get(a[3], "-") + unit[a[3]],
                '9': "ninety" + hyph.get(a[3], "-") + unit[a[3]]}
        
        and_ = {'000': " ",
                '00': " hundred",
                'hun': " hundred and "}
        
        hund = {'0': tens[a[2]],
                'def': unit[a[1]] + and_.get(a[2:], and_['hun']) + tens[a[2]]}
        
        thou = {'0': hund.get(a[1], hund['def']),
                'def': unit[a[0]] + " thousand " + hund.get(a[1], hund['def'])}
        
        number_as_text = thou.get(a[0], thou['def']).strip()
        return number_as_text
    else: print("ERROR: num2test received invalid input.\nREASON: number must",
              "be a positive integer less than or equal to 1000.")
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
def string2score(string):
    """
    Returns the sum of the alphabetical positions of the letters in a string.

    Parameters
    ----------
    string : string
        String to be converted..

    Returns
    -------
    score : integer
        The sum of the alphabetical positions of each letter in a string where:
            A,a = 1
            B,b = 2
            C,c = 3
            etc.

    """
    if isinstance(string, str):
        score = 0
        for char in string.upper():
            value = ord(char) - 64
            value = value if 0 < value <= 26 else 0
            score += value
        return score
    else: print("ERROR: string2score received invalid input.\nREASON: string",
                "be a string. DUH")
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
def sum_digit_power(n, power):
    """
    Raises each digit of the input to the given power and then takes the sum.
    
    Ex: sum_digit_powers(247, 3) = 2^3 + 4^3 + 7^3 = 415

    Parameters
    ----------
    n : integer
        The input integer whose digits will be sum-powered.
    
    power : integer
        The exponent each digit is raised to.
    Returns
    -------
    digit_power_sum : integer
        The result of the described operation.

    """
    if isinstance(n, int) and isinstance(power, (int, float)):
        digit_power_sum = 0
        for digit in str(n):
            digit_power_sum += int(digit) ** power
        return digit_power_sum
    else:
        print("ERROR: sum_digit_power received invalid input.\nREASON: n must",
              "be a positive integer and power must be numeric.")
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
def sum_digit_factorial(n):
    """
    Finds the factorial of each digit of a number and then takes the sum.
    
    Ex: sum_digit_factorial(247) = 2! + 4! + 7! = 5066

    Parameters
    ----------
    n : integer
        The input integer whose digits will be sum-powered.

    Returns
    -------
    digit_factorial_sum : integer
        The result of the described operation.

    """
    if isinstance(n, int):
        digit_factorial_sum = 0
        for digit in str(n):
            digit_factorial_sum += factorial(int(digit))
        return digit_factorial_sum
    else:
        print("ERROR: sum_digit_power received invalid input.\nREASON: n must",
              "be a positive integer and power must be numeric.")