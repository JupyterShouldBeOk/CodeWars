# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 10:17:25 2021

@author: Guilherme

Task:
In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which, for the sake of simplicity, are named with letters from a to m.

The colors used by the printer are recorded in a control string. For example a "good" control string would be aaabbbbhaijjjm meaning that the printer used three times color a, four times color b, one time color h then one time color a...

Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.

You have to write a function printer_error which given a string will return the error rate of the printer as a string representing a rational whose numerator is the number of errors and the denominator the length of the control string. Don't reduce this fraction to a simpler expression.

The string has a length greater or equal to one and contains only letters from ato z.

Examples:
s="aaabbbbhaijjjm"
error_printer(s) => "0/14"

s="aaaxbbbbyyhwawiwjjjwwm"
error_printer(s) => "8/22"
https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python
"""


def printer_error(s):
    x = 0
    error = 0
    n = len(s)
    for i in range (n):
        if ord(s[x]) > 109:
            error = error + 1
        x = x + 1
    return ("%i/%i" %(error,n))
        