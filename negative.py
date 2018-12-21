#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 18:47:22 2018

@author: alireza
"""

from PIL import Image

def negative(tuple_in):
    """(tuple)-> tuple
        
    Returns the negative RGBs as a tuple
    >>> negative((100, 50, 200))
    (155, 205, 55)
    >>> negative((55, 1, 255))
    (200, 254, 0)
    
    """
    list_in = list(tuple_in)
    neg = []
    for i in list_in:
        i = 255 - i
        neg.append(i)
    neg = tuple(neg)    
    return neg

image = Image.open("test_image.jpg")

width = image.size[0]
height = image.size[1]

for x in range(width):
    for y in range(height):
        old_rgb = image.getpixel((x,y))
        new_rgb = negative(old_rgb)
        image.putpixel((x,y), new_rgb)
    
image.save("negative_image.png")