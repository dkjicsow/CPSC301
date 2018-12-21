# -*- coding: utf-8 -*-
"""
Created on Sun Mar 09 15:14:14 2014

@author: mitchell

Created for CPSC 301 2013W2 Lab 08.

This file has some simple functions for reading and writing CSV files.
They are designed to be easily modified.  Note that Python's standard library
has a much more flexible and powerful csv module for working with this format; 
however, its interface is a little intimidating.
"""

import read_write_csv
import matplotlib.pyplot as plt

# In what file is the CSV data?
data_filename = 'trending.csv'
# What character is used to separate the data?
sep = ','

# Should we generate a figure?
create_figure = True

##############################################################################
# Load the data into a list of lists.  Note that there is a header line.
full_list = read_write_csv.read_csv(data_filename, sep, header_line = True)

# Separate the header line from the rest of the data.
header_list = full_list[0]
data_list = full_list[1:]

# Go through the data set and convert all elements except the first column
# (the row labels) into floats.
for i in range(len(data_list)):
  for j in range(1, len(data_list[i])):
    data_list[i][j] = float(data_list[i][j])

##############################################################################
# For each input (column), figure out the summary statistic.

# The first row can serve as our initialization.
# Remember to ignore the first column (the row labels).
summary_values = []
for i in range(len(data_list[0]) - 1):
  summary_values.append(data_list[0][i+1])
 
"""
summ = []
for i in range(len(data_list[0]) - 1):
  summ.append(data_list[0][i+1])
"""
"""
for row in data_list[1:]:
  for i in range(len(summ)):
    summary_values[i] = sum(summ[i], row[i+1])
"""


# Now work through the remaining rows.
for row in data_list[1:]:
  # Remember that summary_values has one fewer entries than the row, since it
  # does not include the first column.
  for i in range(len(summary_values)):
    summary_values[i] = (summary_values[i] + row[i+1])
    
    


"""  
summ = 0
for i in range (0, len(data_list)):
    for j in range(1, len(data_list[i])):
        value = data_list[i][j]
        summ = value + summ
"""
    

##############################################################################
# Print our results.  Remember to ignore that first column.
for i in range(len(summary_values)):
    
    print('Input: ', header_list[i+1], ', Avergaes: ', (summary_values[i]/len(data_list)), sep = '')
  
"""
for i in range(len(summ)):
print('Input: ', header_list[i+1], ', average: ', (summ[i]/10), sep = '')
"""

##############################################################################
# Visualize the result if requested.
if create_figure:
  plt.plot(header_list[1:], summary_values, '-', label = 'average')
  for i in range(len(data_list)):
    plt.plot(header_list[1:], data_list[i][1:], 'o', label = data_list[i][0])
  
  # Add a legend.  The labels in the legend are determined by the label parameters
  # in the calls to plt.plot().  We'll put it in the upper left, since the 
  # general trend of the data is from lower left to upper right.
  plt.legend(loc = "best")
  # Add a title and axis labels.
  plt.xlabel('Input')
  plt.ylabel('Output')
  plt.title('Experimental Results: trending.csv')
  
  # Save the figure.  The image format is determined by the filename extension.
  # We choose png because it uses lossless compression: small filesize without
  # losing any details.
  plt.savefig('trending.png')
  # Close the figure, otherwise matplotlib will continue to add elements to this
  # same figure next time you use plt.plot().
  plt.close()
