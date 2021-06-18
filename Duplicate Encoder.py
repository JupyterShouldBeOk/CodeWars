# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 20:27:53 2021

@author: Guilherme
Task:
The goal of this exercise is to convert a string to a new string where 
each character in the new string is "(" if that character appears only once
 in the original string, or ")" if that character appears more than once in 
the original string. Ignore capitalization when determining if a character is
 a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python
"""

def duplicate_encode(word):
    a =""
    for x in word.lower():
        if word.lower().count(x) > 1:
            a += ")"
        else:
            a += "("
    return a
print(duplicate_encode("cz G k!e !cknGemGGI"))

