# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 23:27:13 2021

@author: Guilherme

Task:
As a part of this Kata, you need to create a function that when provided with a triplet, returns the index of the numerical element that lies between the other two elements.

The input to the function will be an array of three distinct numbers (Haskell: a tuple).

For example:

gimme([2, 3, 1]) => 0
2 is the number that fits between 1 and 3 and the index of 2 in the input array is 0.

Another example (just to make sure it is clear):

gimme([5, 10, 14]) => 1
10 is the number that fits between 5 and 14 and the index of 10 in the input array is 1.
"""

def gimme(val):
    if (val[1] < val[2] and val[0]<val[1]):
        return 1
    elif (val[1] < val[0] and val[2]<val[1]):
        return 1
    elif (val[2] < val[1] and  val[0]<val[2]):
        return 2
    elif (val[2] < val[0] and  val[1]<val[2]):
        return 2
    elif (val[0] < val[1] and  val[2]<val[0]):
        return 0
    else: 
        return 0