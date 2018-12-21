# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 20:29:26 2018

@author: alireza
"""

def bc_income_tax_2018(taxable_income):
    """
    (float)->float
    taxable_income >= 0 and tax_rate > 0 & <= 100
    
    0-39676: tax_rate 5.06
    39676+-79353: tax_rate 7.70
    79353+-91107: tax_rate 10.50
    91107+-110630: tax_rate 12.29
    110630+-150000: tax_rate 14.70
    150000+: tax_rate 16.80
    
    Calculates the total tax (rounded to two decimals places)
    off of a given taxable income using the Tax brackets for BC
    
    >>> bc_income_tax_2018(39676)
    2007.61
    >>> bc_income_tax_2018(79353)
    5062.73
    >>> bc_income_tax_2018(91107)
    6296.9
    >>> bc_income_tax_2018(110630)
    8696.28  
    >>> bc_income_tax_2018(37869.0)
    1916.17
    >>> bc_income_tax_2018(75740.0)
    4784.53
    >>> bc_income_tax_2018(86958.0)
    5861.26
    >>> bc_income_tax_2018(105592.0)
    8077.11
    >>> bc_income_tax_2018(151050.0)
    14660.07
    >>> bc_income_tax_2018(200000.0)
    22883.67
    >>> bc_income_tax_2018(-10000.0)
    Traceback (most recent call last):
        ...
    AssertionError

    
    """
    #tax rates
    rate_1 = 0.0506
    rate_2 = 0.0770
    rate_3 = 0.1050
    rate_4 = 0.1229
    rate_5 = 0.1470
    rate_6 = 0.1680
    
    #tax brackets
    b1 = 0
    b2 = 39676
    b3 = 79353
    b4 = 91107
    b5 = 110630
    b6 = 150000
    
    total_tax = 0 
        
    assert taxable_income >= b1
    
    
    
    if (taxable_income > b1) and (taxable_income <=b2):
        total_tax = rate_1 * taxable_income
    elif (taxable_income > b2) and (taxable_income <=b3):
        total_tax = (rate_1 * b2) + (rate_2 * (taxable_income - b2))
    elif (taxable_income > b3) and (taxable_income <=b4):
        total_tax = (rate_1 * b2) + (rate_2 * (b3-b2)) + (rate_3 * (taxable_income - b3))
    elif (taxable_income > b4) and (taxable_income <=b5):
        total_tax = (rate_1 * b2) + (rate_2 * (b3-b2)) + (rate_3 * (b4-b3)) + (rate_4 * (taxable_income - b4))
    elif (taxable_income > b5) and (taxable_income <=b6):
        total_tax = (rate_1 * b2) + (rate_2 * (b3-b2)) + (rate_3 * (b4-b3)) + (rate_4 * (b5-b4)) + (rate_5 * (taxable_income - b5))
    elif taxable_income > b6:
        total_tax = (rate_1 * b2) + (rate_2 * (b3-b2)) + (rate_3 * (b4-b3)) + (rate_4 * (b5-b4)) + (rate_5 * (b6-b5)) + (rate_6 * (taxable_income - b6))
  
    return round(total_tax, 2)

if __name__ == '__main__':
        import doctest
        doctest.testmod(verbose = True, optionflags = doctest.NORMALIZE_WHITESPACE)
        
    
