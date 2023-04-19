import pandas as pd

# Create a sample DataFrame with a time index
df = pd.DataFrame({'A': [10, 20, 30, 40], 'B': [15, 25, 35, 45]}, index=pd.date_range('2022-01-01', periods=4))

# Calculate the percentage difference between each pair of consecutive entries for each row
pct_diff = df.pct_change()

print(pct_diff)
