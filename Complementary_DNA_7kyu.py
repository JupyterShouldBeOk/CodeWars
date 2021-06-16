# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 23:27:02 2021

@author: Guilherme

Task:
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells 
and carries the "instructions" for the development and functioning of 
living organisms.

If you want to know more http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as 
"C" and "G". You have function with one side of the DNA (string, except 
for Haskell); you need to get the other complementary side. DNA strand is 
never empty or there is no DNA at all (again, except for Haskell).
https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python
"""

def DNA_strand(dna):
    x = "ATGC"
    y = "TACG"
    comp = dna.maketrans(x, y)
    return dna.translate(comp)
