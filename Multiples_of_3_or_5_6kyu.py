# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 11:31:55 2021

@author: Guilherme

Task:
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 
below the number passed in.

Note: If the number is a multiple of both 3 and 5, only count it once. Also, 
if a number is negative, return 0(for languages that do have them)
https://www.codewars.com/kata/514b92a657cdc65150000006/train/python
"""

def solution(number):
    v = 0;
    for c in range(number):
        if c % 3 == 0 or c % 5 == 0:
            v+=c
    return v
print(solution(20))