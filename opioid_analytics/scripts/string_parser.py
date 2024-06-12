import pandas as pd

df = pd.read_csv("../data/interim/merged_df.csv")

# Rename snow to precipsnow to avoid confusion when one-hot encoding
df = df.rename({'snow': 'precipsnow'}, axis=1)

# Come up with preciptype column names
unique_values = set(df['preciptype'].str.split(',').sum())

# For each new preciptype column, 1 if it matches the column name, 0 otherwise
for unique_value in unique_values:
    df[unique_value] = df.apply(lambda row: 1 if unique_value in row['preciptype'] else 0, axis=1)

# Drop preciptype
df.drop(['preciptype'], axis=1, inplace=True)

df.to_csv('../data/interim/preciptype_separated.csv', index=False)
