# -*- coding: utf-8 -*-
"""
Created on Sun Mar 09 12:57:11 2014

@author: mitchell

Modified by: alireza

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
  

def read_csv(filename, sep = ',', header_line = True):
  """(string, string, bool) -> data_list_of_lists
  
  Reads data from a CSV file named filename.  Each line is broken into items by 
  the character(s) in sep.  Each line is returned as a sublist within data_list_of_lists.
  If header_line is True, then the header line is returned as the first sublist.
  """
  
  data_list = []  
  
  with open(filename, 'r') as reader:
    
    next_line = get_next_line(reader)

    if header_line and next_line:
      # Read the header line and process it differently if necessary.
      header_list = split_line(next_line, sep)
      data_list.append(header_list)
      next_line = get_next_line(reader)
      
    # If we have not reached the end of the file, read another line and process it.
    while next_line:
      element_list = split_line(next_line, sep)
      data_list.append(element_list)
      next_line = get_next_line(reader)
    
    return data_list


def write_elements(writer, data_list, sep = ', '):
  """(file open for writing, list, string) -> None
  
  The elements of data_list are written to the file with sep between them.
  A newline is added at the end.
  """

  # We want the separator character(s) after every item except the last one.
  for item in data_list[:-1]:
    writer.write(item)
    writer.write(sep)
    
  # After the last item, write a newline.
  writer.write(data_list[-1])
  writer.write('\n')
  
  
def write_csv(filename, data_list_of_lists, sep = ', '):
  """(string, list of lists, string) -> None
  
  Writes data to a CSV file named filename.  Each sublist of data_list_of_lists
  is written on a separate line.  Each element of each sublist is separated
  by sep.
  """
  
  with open(filename, 'w') as writer:
    for row in data_list_of_lists:
      write_elements(writer, row, sep)
      
