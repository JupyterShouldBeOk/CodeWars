# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 10:18:22 2021

@author: Guilherme
Task:
You will be given an array of numbers. You have to sort the odd numbers 
in ascending order while leaving the even numbers at their original positions.
https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python
"""
def sort_array(num):
    a = 0; e = 0;  temp = 0;
    while a <= (len(num)-1):
        while e <= (len(num)-1):
            if ((num[a] % 2 != 0) and (num[e] % 2 != 0)):
                if ((num[e] < num[a])and ( a < e)):
                    temp = num[a]
                    num[a] = num[e]
                    num[e] = temp
                elif ((num[a] < num[e])and ( e < a)):
                    temp = num[e]
                    num[e] = num[a]
                    num[a] = temp                
            e += 1   
        if e == len(num): e = 0    
        a += 1
    return num



        
