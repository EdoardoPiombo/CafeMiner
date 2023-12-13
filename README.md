# Requirements
To run the program you need Python3, with the modules pandas and argparse.
The program was tested with Python 3.11.3, pandas 2.0.0 and argparse 1.5.3.

# What does it do?
The script will use the CAFE5 output files "Base_branch_probabilities.tab" and "Base_change.tab" to calculate the number of gene family expansions and contractions, at every node, that are significant according to a specified Pvalue threshold.
The output file will be very similar to the CAF5 output file "Base_clade_results.txt", but instead of counting all expansions and contractions it will only consider the ones that were significant.

# Input files
The main input is a results folder produced by CAFE5.
Moreover, the user will need to specify a Pvalue threshold necessary to determine which gene families are significantly expanded or contracted.
