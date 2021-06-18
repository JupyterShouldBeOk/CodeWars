# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 14:12:58 2021

@author: Guilherme
Task:
Move the first letter of each word to the end of it, then add "ay" to the end 
of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python
"""

def pig_it(text):
    a=[]
    for x in text.split(" "):
        if x == "?" or x == "!" or x == ".":
            a.append(x)
        else:
            a.append(x[1:len(x):1]+x[0:1:1]+"ay")
    return " ".join(a)
        
print(pig_it('Hello world !'))