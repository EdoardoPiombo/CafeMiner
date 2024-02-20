import pandas as pd
import argparse as ap

#arguments
parser = ap.ArgumentParser()
parser.add_argument("-f", "--folder", help="input name of the folder with CAFE results")
parser.add_argument("-t", "--threshold", help="Input the Pvalue threshold you want to use to consider an expansion or contraction to be significant")
parser.add_argument("-o", "--output", help="name of the output table containing the number of significant expansions or contractions at every node")


args = parser.parse_args()

CAFEfold = args.folder
threshold = float(args.threshold)
output = args.output



#I load a dataframe with the Pvalues calculated at each node for each family
prob = pd.read_csv(f"{CAFEfold}/Base_branch_probabilities.tab", sep = '\t', index_col='FamilyID')
#I turn 'N/A' into 1
prob.applymap(lambda x: float(1) if x == 'N/A' else x)

#I load a dataframe with the name of changes in family number at every node
change = pd.read_csv(f"{CAFEfold}/Base_change.tab", sep = '\t', index_col='FamilyID')

#I make a result dataframe filled with zeroes, which will increase as the program runs
results = pd.DataFrame(index=prob.columns, columns=['Significant Increase', 'Significant Decrease'], data = 0)

#For every family, if its change is significant at a specific node, according to the specified threshols,
#I will add 1 to the Increase of Decrease count, depending on if the change is positive or negative
for ele in prob.index.tolist():
    for tax in prob.columns.tolist():
        if prob.loc[ele, tax] < threshold :
            if change.loc[ele, tax] > 0:
                results.loc[tax, 'Significant Increase'] += 1
            elif change.loc[ele, tax] < 0:
               results.loc[tax, 'Significant Decrease'] += 1 

#The results are exported
results.index.name = "#Taxon_ID"
results.to_csv(output, sep= '\t')
            
    
