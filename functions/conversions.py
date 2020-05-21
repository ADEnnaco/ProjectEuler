# -*- coding: utf-8 -*-
# conversions.py>
"""
Functions for converting between different units or data types

"""
def num2text(number):
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
    
    return thou.get(a[0], thou['def']).strip()