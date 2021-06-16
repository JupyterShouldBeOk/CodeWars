# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 12:55:48 2021

@author: Guilherme
Task:
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.
https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python
"""

def find_uniq(digits):
    g = digits[0]
    for c in digits:
        if g != c:
            if digits.count(g) == 1:
                return g; break
            else: 
                return c; break
        g = c
