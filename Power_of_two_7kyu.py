# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 13:33:09 2021

@author: Guilherme
Task:
omplete the function power_of_two/powerOfTwo (or equivalent, depending on your 
language) that determines if a given non-negative integer is a power of two. 
From the corresponding Wikipedia entry:

a power of two is a number of the form 2n where n is an integer, i.e. the 
result of exponentiation with number two as the base and integer n as the 
exponent.

You may assume the input is always valid.

Examples
power_of_two(1024) ==> True
power_of_two(4096) ==> True
power_of_two(333)  ==> False
https://www.codewars.com/kata/534d0a229345375d520006a0/train/python
"""


def power_of_two(x):
    i = 1
    while i < 2000:
        a = x**(1/i)
        if (a == 2 and a**i == x) or x == 1:
            print(a,i)
            return True
        i+=1
    return False
print(power_of_two(1267650600228229401496703205372))
        
        





