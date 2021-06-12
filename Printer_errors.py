# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 10:17:25 2021

@author: Guilherme
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
        