# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 22:37:59 2021

@author: Guilherme
"""

def calculate_years(principal, interest, tax, desired):
    years = 0
    while principal < desired:
            principal += (principal*interest*(1-tax))
            years = years + 1
    print(years)
    return years


            
      
        