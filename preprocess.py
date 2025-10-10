import pandas as pd

csv = pd.read_csv(
    "HappinessData-1.csv",
    na_values=["NA", "N/A", "", " "],
    keep_default_na=True
)

# Move the class label column to be the last column in the csv file.
target_column = 'Unhappy/Happy'
cols = [col for col in csv.columns if col != target_column]

for col in cols:
    csv[col] = pd.to_numeric(csv[col], errors="coerce")
csv[target_column] = pd.to_numeric(csv[target_column], errors='coerce').astype("Int64")

# Drop missing values
cols_with_missing = ["Quality of schools", "Community trust in local police"]
existing = [col for col in cols_with_missing if col in csv.columns]

if existing:
    csv = csv.dropna(subset=existing)
else:
    csv = csv.dropna(subset=cols)

csv[cols] = csv[cols].astype(float)
csv[target_column] = csv[target_column].astype(int)

# -- Correlations -- 
feature_correlation = csv[cols].corr(method="pearson")
target_correlations = csv[cols].corrwith(csv[target_column].sort_values(ascending=False))
print("Top feature target correlations: ")
print(target_correlations.head(10))

# Export to new CSV
csv.to_csv('processed.csv', index=False)
print("Processed Dataset, saved as 'process.csv'. ")