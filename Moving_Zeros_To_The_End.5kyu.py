# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 14:32:31 2021

@author: Guilherme
Task:
Write an algorithm that takes an array and moves all of the zeros to the end, 
preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python
"""

def move_zeros(array):
    a = []
    i = 0
    for x in array:
        if x != 0:
            a.append(x)
    while i < array.count(0):
       a.append(0)
       i+=1
    return a
print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))





 
            
            