# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 13:33:09 2021

@author: Guilherme
Task:
Complete the solution so that the function will break up camel casing, using 
a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
https://www.codewars.com/kata/5208f99aee097e6552000148/train/python
"""


def solution(s):
    a =""
    for c in s:
        if not c.isupper(): 
            a += c
        elif c.isupper():
            a = a + " " + c
    return a
        
        






