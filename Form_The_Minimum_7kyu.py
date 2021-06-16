# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 12:19:33 2021

@author: Guilherme
Task
Given a list of digits, return the smallest number that could be formed from these digits,
using the digits only once (ignore duplicates).

Notes:
Only positive integers will be passed to the function (> 0 ), no negatives or zeros.
Input >> Output Examples
minValue ({1, 3, 1})  ==> return (13)
Explanation:
(13) is the minimum number could be formed from {1, 3, 1} , Without duplications

minValue({5, 7, 5, 9, 7})  ==> return (579)
Explanation:
(579) is the minimum number could be formed from {5, 7, 5, 9, 7} , Without duplications

minValue({1, 9, 3, 1, 7, 4, 6, 6, 7}) return  ==> (134679)
Explanation:
(134679) is the minimum number could be formed from {1, 9, 3, 1, 7, 4, 6, 6, 7} , Without duplications
https://www.codewars.com/kata/5ac6932b2f317b96980000ca/train/python
"""

def min_value(digits):
    b = sorted(set(digits))
    v = 0
    i = 0
    while i <= len(b)-1:
        v+=b[i]*(10**(len(b)-i-1))
        i+=1    
    return v   

