# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 16:59:01 2021

@author: Guilherme

Task:
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.
https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python
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
   