# -*- coding: utf-8 -*-
"""
@author: mitchell

changed on Feb 28, 2017 by dawson
changed on Dec 6, 2017 by Jerry Jim
Modified by: alireza
"""
import calendar

def find_next_year(start_year, the_month, the_day, the_weekday):
  """(int, int, int, int) -> int
  
  Preconditions:
    start_year >= 2018
    1 <= the_month <= 12
    1 <= the_day <= 31
    0 <= the_weekday < 7
    
  Returns the first year at or after start_year in which the date 
  the_month, the_day falls on the day of the week the_weekday.  Note
  that the_weekday follows Python's calendar module standard: Monday is 0
  Tuesday is 1, ..., Sunday is 6.
  
  Examples:
  >>> find_next_year(2018, 8, 25, 5)
  2018
  >>> find_next_year(2020, 1, 1, 2)
  2020
  >>> find_next_year(2021, 1, 1, 2)
  2025
  >>> find_next_year(2016, 2, 29, 0)
  2016
  >>> find_next_year(5432, 2, 28, 3)
  5433
  """
  
  current_year = start_year
  
   
  
  if calendar.weekday(current_year,the_month,the_day) == the_weekday:
      return current_year
  else:
      current_year += 1
      
  while calendar.weekday(current_year, the_month, the_day) != the_weekday:
      current_year += 1
  return current_year
