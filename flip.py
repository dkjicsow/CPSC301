#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 18:12:49 2018

@author: alireza
"""

from PIL import Image

image = Image.open("test_image.jpg")
width = image.size[0]
height = image.size[1]
flip = Image.new('RGB', (width, height))

for x in range(width):
    for y in range(height):
        colour = image.getpixel((x,y))
        new_y = height - y - 1
        xy = (x, new_y)
        flip.putpixel(xy, colour)
flip.save("flip_image.png")