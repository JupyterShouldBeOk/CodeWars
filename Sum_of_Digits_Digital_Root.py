# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 22:51:38 2021

@author: Guilherme
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