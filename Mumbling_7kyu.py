# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 00:51:19 2021

@author: Guilherme
Task:
This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python
"""
def accum(s):
    a=""
    i = 0
    for c in s.lower():
        a = a + c.upper() + i*c
        i = i + 1
        if (i > 0 and i < len(s)) :
            a = a + "-"
    return a


