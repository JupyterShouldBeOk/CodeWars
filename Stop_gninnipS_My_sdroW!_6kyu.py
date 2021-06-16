# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 11:31:55 2021

@author: Guilherme
Task:
Write a function that takes in a string of one or more words, and returns 
the same string, but with all five or more letter words reversed (like the 
name of this kata).

Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.
Examples:

spinWords("Hey fellow warriors") => "Hey wollef sroirraw" 
spinWords("This is a test") => "This is a test" 
spinWords("This is another test") => "This is rehtona test"
https://www.codewars.com/kata/5264d2b162488dc400000001/train/python
"""

def spin_words(s):
    b = s.split(" ")
    d = ""
    for k, v in enumerate(b):
        if len(v) >= 5:
            v = v[::-1]
        if k == len(b)-1:
            d+= v
        else:
            d += v + " "         
    return d


    
