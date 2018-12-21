"""
aa_counter.py: A simple Python program which counts the number of each
essential amino acid that appears in a protein sequence FASTA file. Other
amino acids (or incorrect codes) are also counted in a general bin.

Input: a FASTA file containing a protein sequence. If the file
contains multiple sequences, only the first is analyzed.

Output: A brief table summarizing the number of each essential amino acid
that was found in the sequence.
"""

# Created by Ryan Giuliany for CPSC 301, summer 2009.
# Modified by Ian Mitchell, January 2010.
# Further modified by Jay Zhang, January 2011.
# Further modified by Ian Mitchell, January 2014 to convert into functions.
# Validated by J. Jim Oct 2018

def readFasta(filename):
  """(string) -> string
  
  Opens filename in the current directory.  If it starts with a FASTA header,
  return the first sequence found in that file as a string (with whitespace removed).
  """
  
  with open(filename) as seq_file:
    first_line = seq_file.readline()
    first_line = first_line.strip()
    if first_line[0] == ">":
      print("Reading sequence: " + first_line[1:])
    else:
      print("First line does not begin with '>' so the file is not in FASTA format.")
      exit("Format Error")
    output = ""
    for seq_line in seq_file:
      seq_line = seq_line.strip()
      if(len(seq_line) == 0):
        continue
      if seq_line[0] == ">":
        print("Warning: Multiple sequences encountered; only the first is returned.")
        break;
      output = output + seq_line
  return output


def count_dna(sequence):
  """(string) -> boolean
  
  Counts the number of each essential amino acid which appears in a sequence string.
  Prints the results and returns True.
  """
  
  # Set up all our counters. Note: other_count counts miscellaneous amino acids
  # that are not counted by our program.
  A_count = 0
  T_count = 0
  C_count = 0
  G_count = 0
  other_count = 0
  
  # We could hardcode the single character code for each AA in the if statements
  # below, but hardcoded constants are considered poor programming style.
  # Instead, we will create variables with meaningful names which store the
  # constants; in that way it is easier to understand what the if statements
  # below are doing. Note that we do not need a variable for "other"; that
  # counter will appear in the else block of our if statements below.
  adenine_short = "A"
  thymine_short = "T"
  cytosine_short = "C"
  guanine_short = "G"

  
  # Look through each character in the sequence and count the ones corresponding
  # to essential amino acids.
  for deoxyribonucleic_acid in sequence:
      if deoxyribonucleic_acid == adenine_short:
          A_count = A_count + 1
      elif deoxyribonucleic_acid == thymine_short:
          T_count = T_count + 1
      elif deoxyribonucleic_acid == cytosine_short:
          C_count = C_count + 1
      elif deoxyribonucleic_acid == guanine_short:
          G_count = G_count + 1
      else:
          other_count = other_count + 1
  
  # All done counting! We've finished counting the first sequence in the 
  # FASTA file.  Our analysis is complete and we can just print the results
  print("Deoxyribonucleic Acid counts")
  print("Adenine: " + str(A_count))
  print("Thymine: " + str(T_count))
  print("Cytosine: " + str(C_count))
  print("Guanine: " + str(G_count))
  print("Other: " + str(other_count))

  # It would be nice to return the counts, but we don't yet have a way of
  # returning that much data.  We'll return True to let the caller know
  # That everything is okay.
  return True

if __name__ == '__main__':
  
  # Ask the user for a FASTA file containing a protein sequence.
  filename = input("Enter the FASTA file you wish to count: ")
  
  # Use the functions above to read and count the essential amino acids.
  readFasta(filename)
  count_dna(readFasta(filename))
