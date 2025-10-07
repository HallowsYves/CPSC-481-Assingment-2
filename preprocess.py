import pandas as pd

# Load the CSV
csv = pd.read_csv("HappinessData-1.csv")

# Move the class label column to be the last column in the csv file.
col_to_move = 'Unhappy/Happy'
other_cols = [col for col in csv.columns if col != col_to_move]
new_column_order = other_cols + [col_to_move]
csv = csv[new_column_order]

# Remove missing values for Quality of schools and Community Trust in local Police
csv = csv.dropna(axis='index')