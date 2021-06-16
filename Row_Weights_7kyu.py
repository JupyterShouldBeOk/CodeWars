# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 16:23:18 2021

@author: Guilherme
Task:
Several people are standing in a row divided into two teams.
The first person goes into team 1, the second goes into team 2, 
the third goes into team 1, and so on.

Given an array of positive integers (the weights of the people), 
return a new array/tuple of two integers, where the first one is the total 
weight of team 1, and the second one is the total weight of team 2.
https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9/train/python
"""
def row_weights(array):
    i = 0; a = 0; b = 0;
    while i < len(array):
        if (i % 2 == 0):
            a += array[i]
        elif (i % 2 != 0):
            b += array[i]
        i +=1
    return a, b