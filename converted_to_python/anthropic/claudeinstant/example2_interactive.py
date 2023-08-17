import pandas as pd

df = pd.read_csv('your_file_path')

# Convert selected columns to strings   
df['var1'] = df['var1'].astype(str)
df['var2'] = df['var2'].astype(str) 
df['var3'] = df['var3'].astype(str)

# Keep var4 and var5 as numeric

# Save the reformatted data
df.to_csv('reformatted_data.csv', index=False)

This does the following:

1. Reads the input file into a Pandas DataFrame using read_csv
2. Converts the var1, var2 and var3 columns to strings using astype(str)
3. var4 and var5 remain numeric 
4. Saves the reformatted data to a CSV file using to_csv