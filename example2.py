import pandas as pd

# Read in the data
df = pd.read_csv('your_file_path')

# Convert selected variables to strings
df['var1'] = df['var1'].astype(str)
df['var2'] = df['var2'].astype(str)
df['var3'] = df['var3'].astype(str)

# Keep var4 and var5 as numeric

# Output the reformatted data
df.to_csv('reformatted_data.csv', index=False)