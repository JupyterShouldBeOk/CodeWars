# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 16:59:01 2021

@author: Guilherme
Task:
The rgb function is incomplete. Complete it so that passing in RGB decimal 
values will result in a hexadecimal representation being returned. Valid 
decimal values for RGB are 0 - 255. Any values that fall out of that range 
must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will
 not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
https://www.codewars.com/kata/513e08acc600c94f01000001/train/python
"""
def rgb(r, g, b):
    l = [r,g,b]
    a = []
    for i in l:
        if i > 255:
            a.append('{0:02x}'.format(int(255)))
        elif i < 0:
            a.append('{0:02x}'.format(int(0)))
        else:
            a.append('{0:02x}'.format(int(i)))
    return "".join(a).upper()


