# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 19:14:30 2021

@author: Guilherme
Task:
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python
"""

def find_it(seq):
    for c in seq:
        if seq.count(c) % 2 == 1:
            return c
