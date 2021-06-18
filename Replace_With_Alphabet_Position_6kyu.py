# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 00:45:36 2021

@author: Guilherme
Task:
Welcome.

In this kata you are required to, given a string, replace every letter with
 its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 
15 3 11" (as a string)
https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python
"""
def alphabet_position(text):
    a= []
    for x in text:
        if 97 <= ord(x) <= 122:
            a.append(str(ord(x) - 96))
        elif 65 <= ord(x) <= 90:
            a.append(str(ord(x) - 64))
    return " ".join(a)
   