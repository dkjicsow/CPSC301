# -*- coding: utf-8 -*-
"""
@author: mitchell

Updated by : tsiknis, dawson, j. jim
"""

def text_triangle(height):
    """(int) -> string
    
    Returns a text version of an isosceles triangle built from 'X' characters
    with height copies of the X in the longest line.  The triangle is returned
    in a multiline string.  The string is empty if height <= 0.
    
    For instance, if we call print(text_triangle(5))it will print the following:
    X
    XX
    XXX
    XXXX
    XXXXX
    XXXX
    XXX
    XX
    X
    
    >>> text_triangle(1)
    'X\\n'
    >>> text_triangle(2)
    'X\\nXX\\nX\\n'
    >>> text_triangle(3)
    'X\\nXX\\nXXX\\nXX\\nX\\n'
    >>> text_triangle(5)
    'X\\nXX\\nXXX\\nXXXX\\nXXXXX\\nXXXX\\nXXX\\nXX\\nX\\n'
    
    """
    
    if(height <= 0):
        return ''
    else:
        out_string = ''
        for i in range(1, height):
            out_string += 'X' * (i) + '\n'
        for i in range(height, 0, -1):
            out_string += 'X' * i + '\n'
        return out_string


if __name__ == '__main__':
        import doctest
        doctest.testmod(verbose = True, optionflags = doctest.NORMALIZE_WHITESPACE)