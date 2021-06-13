# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 22:51:38 2021

@author: Guilherme

Task:
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

Examples
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
"""
def digital_root(n):       
    for i in range (10):
        a = n//(10**5)
        b = n//(10**4)-(a*10)
        c = n//(10**3)-(a*100)-(b*10)
        d = n//(10**2)-(a*1000)-(b*100)-(c*10)
        e = n//(10**1)-(a*10000)-(b*1000)-(c*100)-(d*10)
        f = n//(10**0)-(a*100000)-(b*10000)-(c*1000)-(d*100)-(e*10)
        n = a+b+c+d+e+f
        if n<10:
            return n
            break;  