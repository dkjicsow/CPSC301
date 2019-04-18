# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 22:32:23 2014

@author: mitchell
Updated by tsiknis on Jan 20, 2016
Updated by Oliver Zhang on Jan 23, 2017
  - updated to 2017 brackets
  - renamed next to nextBracket so as to avoid conflict with built in function
Updated by J. Jim on Jan 15, 2018
  - updated numbers to reflect Revenue Canada latest data
Checked by J. Jim on Sept 23, 2018
Modified by: alireza
"""

def not_death(foo):
    """
    (float)->float
    Foo is an indiviauls annual income. The function will return a summ of all
    the taxes
    
    foo>0
    
    >>>not_death(205842)=47669.79
    >>>not_death(144489)=29877.42
    >>>not_death(93208)=16544.36
    >>>not_death(46605)=6990.75
    >>>not_death(2)=0.3


    
    """
    next_bracket = foo - 205842.0
    bar = max(0, next_bracket * 0.04)
    next_bracket = foo - 144489.0
    bar += max(0, next_bracket * 0.03)
    next_bracket = foo - 93208.0
    bar += max(0, next_bracket * 0.055)
    next_bracket = foo - 46605.0
    bar += max(0, next_bracket * 0.055)
    bar += foo * 0.15
    bar = round(bar, 2)
    return bar
