# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 13:33:09 2021

@author: Guilherme

Task:
Given an array of integers of any length, return an array that has 1 added to
the value represented by the array.

the array can't be empty
only non-negative, single digit integers are allowed
Return nil (or your language's equivalent) for invalid inputs.

Examples
For example the array [2, 3, 9] equals 239, adding one would return the array 
[2, 4, 0].

[4, 3, 2, 5] would return [4, 3, 2, 6]
https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9/train/python
"""

def up_array(arr):
    if len(arr) == 0:
        return None
    for c in arr:
        if c < 0 or c > 9:
            return None
    if 10 > arr[-1] >= 0:
        arr[-1] +=1
        i=1
        while i <= len(arr)-1:
            if arr[-i] == 10:
                arr[-i] = 0; arr[-i-1]+=1;
            i+=1
        if arr[0] == 10:
            arr[0] = 0
            arr = [1] + arr
        return arr
    return None





