import pandas as pd

# Read in data
df = pd.read_csv('data.csv')

# Check for missing values
print(df.isnull().sum())

# Remove outliers
df = df[df['column_name'] < 100]

# Transform variables
df['new_column'] = df['column_name'] * 2
