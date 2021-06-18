# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 19:07:17 2021

@author: Guilherme
Task:
Write a function that takes a string of parentheses, and determines if the
 order of the parentheses is valid. The function should return true if the 
 string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
"""

def valid_parentheses(string):
    a=[]
    for x in string:
        if x == "(" :
            a.append(x) 
        elif x == ")":
            if len(a) >= 1:
                a.pop(-1)
            else:
                return False
    if len(a) == 0:
        return True
    else:
        return False


  
