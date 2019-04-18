# -*- coding: utf-8 -*-
"""
CPSC 301 2018W1 Lab 04.

right_triangle.py skeleton.

This file contains spots where students can type their functions 
find_other_angle(), find_hypotenuse(), find_opposite() and describe_triangle().

@author: Ian Mitchell

Modified by: alireza
"""
from math import cos
from math import sqrt
from math import radians
####################################################
# Here is a spot to create find_other_angle().
####################################################
def find_other_angle (angleθ):
    """
    (float)->float
    angleθ is < 90 and > 0
    
    Calculates the other angleϕ in degrees when given angleθ in degrees for 
    a right angle triangle with 90 degrees 
    
    >>>find_other_angle(30)=60
    >>>find_other_angle(45)=45
    >>>find_other_angle(36.87)=53.13
    """
    angleθ = (90-angleθ)
    
    return angleθ



####################################################
# Here is a spot to create find_hypotenuse().
####################################################
def find_hypotenuse(angleθ,adj_length):
    """
    (float,float)->float
    angleθ is < 90 and > 0 and adj_length is length of side adjacent to angleθ
    and is > 0
    
    Calculates the length of the hypotenuse of a right angle triangle 
    given angleθ in degrees and adj_length
    
    >>>find_hypotenuse(45,1)=from math import sqrt(2)
    >>>find_hypotenuse(60,1)=2
    >>>find_hypotenuse(36.87,4)=5
    """
    return adj_length / cos(angleθ)
    
####################################################
# Here is a spot to create find_opposite().
####################################################
def find_opposite(angleθ,adj_length):
    """
    (float,float)->float
    angleθ is < 90 and > 0 and adj_length is length of side adjacent to angleθ
    and is > 0
    
    Calculates the length of the opposite side of a right angle triangle 
    given angleθ in degrees and adj_length
    
    >>>find_opposite(45,1)=1
    >>>find_hypotenuse(60,1)=from math import sqrt(3)
    >>>find_hypotenuse(36.87,4)=3
    """
    return sqrt(((adj_length/cos(radians(angleθ)))**2)+(adj_length)**2)

####################################################
# Here is a spot to create describe_triangle().
####################################################
def describe_triangle(find_other_angle, find_hypotenuse, find_opposite):
    """
    (float,float)->float
    
    
    Summary of the triangle including the lengths and angles
    
    >>>find_opposite(45,1)=1
    >>>find_hypotenuse(60,1)=from math import sqrt(3)
    >>>find_hypotenuse(36.87,4)=3
    """
    print ('Angle theta (degrees) = ', find_other_angle)
    print ('Angle phi (degrees) = ', (90-find_other_angle))
    print ('Length of hypotenuse = ', find_hypotenuse)
    print ('Length of edge adjacent to theta = ', )
    print ('Length of edge adjacent to phi = ', find_opposite)
    
    
    return None

