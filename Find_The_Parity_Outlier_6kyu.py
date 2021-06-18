# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 17:55:04 2021

@author: Guilherme
Task:
You are given an array (which will have a length of at least 3, but could be 
very large) containing integers. The array is either entirely comprised of odd 
integers or entirely comprised of even integers except for a single integer N. 
Write a method that takes the array as an argument and returns this "outlier" 
N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python
"""

def find_outlier(integers):
    odd=[]
    even=[]
    for x in integers:
        if x%2 == 0:
            odd.append(x)
        else:
            even.append(x)
    if len(odd) == 1:
        return odd[0]
    else:
        return even[0]

        
        
        
        