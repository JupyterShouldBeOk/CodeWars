# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 17:56:43 2021

@author: Guilherme
Task:
In this simple Kata your task is to create a function that turns a string into 
a Mexican Wave. You will be passed a string and you must return that string 
in an array where an uppercase letter is a person standing up.
1.  The input string will always be lower case but maybe empty.
2.  If the character in the string is whitespace then pass over it as if it was an empty seat
Example: wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/train/python
"""

def wave(txt):
    a = list(range(0, len(txt), 1))
    i = 0
    d = 0
    while i <= len(txt) - 1:
        a[i] = txt[0:i:1] + txt[i].upper() + txt[i+1:len(txt):1]
        i+=1
    while d <= len(a) - 1:
        if a[d] == txt:
            a.pop(d)
            d -=1
        d +=1
    return a


        
