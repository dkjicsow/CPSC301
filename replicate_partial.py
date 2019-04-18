# -*- coding: utf-8 -*-
"""
Created on Tue Feb 04 15:41:19 2014

@author: mitchell

Created for CPSC 301 2013W2, Lab 05

Verified by Jim for CSPC 301 2018W1

Modified by: alireza

"""

def replicate_dna(in_strand):
  """(string) -> string
  
  The input is a single DNA strand described in terms of its bases (a, c, g, t).
  The output is the matching complementary DNA strand.  Characters in the input
  which are not one of the standard bases are replaced by the 'x' character.
  
  >>>replicate_dna('acgt')
  'tgca'
  >>>replicate_dna('aaccggttaacagataacccgctcagcgggtgatctgttt')
  'ttggccaattgtctattgggcgagtcgcccactagacaaa'
  >>>replicate_dna('abcdefghijklmnopqrstuvwxyz0123456789~!@#$%^&*()_+')
  'txgxxxcxxxxxxxxxxxxaxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
  """
  
  out_strand = ''
  for base in in_strand.lower():
    if base == 'a':
      out_strand += 't'
    elif base == 't':
        out_strand += 'a'
    elif base == 'g':
        out_strand += 'c'
    elif base == 'c':
        out_strand += 'g'
    else:
      out_strand += 'x'
  return out_strand
  

print(replicate_dna("acgtacgtacgt"))
