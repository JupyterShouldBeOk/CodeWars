# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 16:59:01 2021

@author: Guilherme
"""
def disemvowel(s):
    x = 0
    a = ''
    while x < (len(s)):
        if (s[x] == 'a' or s[x] == 'e' or s[x] == 'i' or s[x] == 'o' or s[x] == 'u' or s[x] == 'A' or s[x] == 'E' or s[x] == 'I' or s[x] == 'O' or s[x] == 'U'):
            a = a + ''
        else: 
            a = a + s[x]
        x = x + 1
    return a
   