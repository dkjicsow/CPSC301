 #-*- coding: utf-8 -*-
"""
Created on Sun Mar 09 12:57:11 2014

@author: mitchell

Created for CPSC 301 2013W2 Lab 09.

This file has some simple functions for reading and writing CSV files.
They are designed to be easily modified.  Note that Python's standard library
has a much more flexible and powerful csv module for working with this format; 
however, its interface is a little intimidating.
"""

def get_next_line(reader):
  """(file open for reading) -> string or None
  
  Read the next non-blank line from a file and return it as a string after
  stripping all leading and trailing whitespace.  A "non-blank line" is a line
  which contains some character(s) other than whitespace.  None is returned
  if there are no more lines to read.
  """

  # Read lines from the file until a line is found which is not empty.
  line = ''
  while not line:
    # Read the next line.
    line = reader.readline()
    # If an empty string is returned, there are no more lines.
    if not line:
      return None
    else:
      # Otherwise remove whitespace from the line.  If the line contains only 
      # whitespace (eg: it would appear blank in a text editor), this operation
      # will result in an empty string.
      line = line.strip()

  return line


def split_line(line, sep = ','):
  """(string, string) -> list:

  Break a string into a list at some separator character(s).  Resulting elements
  are stripped of leading and trailing whitespace and then returned in a list
  of strings.
  """
  
  # Break line into elements at the separator character.
  elements = line.split(sep)
  
  # Remove any leading or trailing whitespace.
  for i in range(len(elements)):
    elements[i] = elements[i].strip()
    
  return elements
  

def read_co2ghg():
  """(string, string, bool) -> data_list_of_lists
  
  Reads data from a CSV file named filename.  Each line is broken into items by 
  the character(s) in sep.  Each line is returned as a sublist within data_list_of_lists.
  If header_line is True, then the header line is returned as the first sublist.
  """
  data_list = []  
  filename = 'co2ghg_wrong.csv'
  sep = ';'
  
  with open(filename, 'r') as reader:
    
    next_line = get_next_line(reader)

    if next_line:
      # Read the header line and process it differently if necessary.
      header_list = split_line(next_line, sep)
      data_list.append(header_list)
      next_line = get_next_line(reader)
     # If we have not reached the end of the file, read another line and process it.
  
    #went through every year 1990-2005 (only shows 2005)
 
    while next_line:
         year_list = []
         sep = '  ' 
         element_list = split_line(next_line, sep)
         year_list.extend(element_list)
    
         country_list = [] 
         for i in range(len(year_list)):
             sep = ';'
             smaller_list = split_line(year_list[i], sep)
             country_list.append(smaller_list)
         data_list.extend(country_list)
         next_line = get_next_line(reader)
    return data_list

def filter_keep_country(data_list_of_lists, which_country):
    filtered_list_of_lists = []
    for i in range(len(data_list_of_lists)):
        if data_list_of_lists[i][0] == which_country:
            filtered_list_of_lists.append(data_list_of_lists[i])
    return filtered_list_of_lists

def filter_delete_column(data_list_of_lists, which_column):
    filtered_list_of_lists = data_list_of_lists[:]
    for i in range(len(data_list_of_lists)):
        filtered_list_of_lists[i].remove([which_column])
    return filtered_list_of_lists   
    
data_list_of_lists = read_co2ghg()
filtered = filter_keep_country(read_co2ghg(), 'Canada')
deleted = filter_delete_column(read_co2ghg(), 2)

import read_write_csv
read_write_csv.write_csv('co2ghg.csv', data_list_of_lists, sep = ',')

if __name__ == '__main__':
  import doctest
  doctest.testfile('co2ghg_filter_test.txt')




