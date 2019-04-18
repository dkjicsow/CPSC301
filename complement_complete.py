# -*- coding: utf-8 -*-
"""
@author: mitchell

Modified by: alireza
"""

from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

def complement_dna(in_strand, report_counts = False):
  """(string, boolean) -> string

  Precondition: in_strand may only contain characters 'a', 'c', 'g', or 't'
  (or 'A', 'C', 'G', 'T').
  
  The input is a single DNA strand described in terms of its bases (a, c, g, t).
  The output is the matching complementary DNA strand.
  The output is always lower case.
    
  If report_counts is True, then a count of how many times each of the bases
  appears in in_strand is printed to the screen.

  >>> complement_dna('acgt')
  'tgca'
  >>> complement_dna('aaccggttaacagataacccgctcagcgggtgatctgttt')
  'ttggccaattgtctattgggcgagtcgcccactagacaaa'
  >>> complement_dna('aaccggttaacagataacccgctcagcgggtgatctgttt', True)
  Number of base a: 10
  Number of base c: 10
  Number of base g: 10
  Number of base t: 10
  ttggccaattgtctattgggcgagtcgcccactagacaaa
  """

  # Convert the input string into a Seq object.
  # Use lower cases characters for consistency.
  in_seq = Seq(in_strand.lower(), generic_dna)
  
  out_seq = in_seq.complement()
  
  A = in_seq.count('a')
  C = in_seq.count('c')
  G = in_seq.count('g')
  T = in_seq.count('t')
      
  if report_counts == True:
            print ('Number of base a: ',A,'\nNumber of base c: ',C,'\nNumber of base g: ',G,'\nNumber of base t: ',T,'\n'+str(out_seq))
                   

  else:
      return str(out_seq)
      
  # Convert the output Seq object into a string and return it.  
  
  
if __name__ == '__main__':
  import doctest
  # When you think your code is operational, you can uncomment the following
  # line to allow doctest to run.
  doctest.testmod(verbose = True, optionflags = doctest.NORMALIZE_WHITESPACE)
