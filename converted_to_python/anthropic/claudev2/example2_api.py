import pandas as pd

# Read in the data 
df = pd.read_csv('your_file_path')

# Convert selected columns to strings
df['var1'] = df['var1'].astype(str) 
df['var2'] = df['var2'].astype(str)
df['var3'] = df['var3'].astype(str) 

# Keep var4 and var5 as numeric

# Output the reformatted DataFrame
reformatted_df = df
```

The key steps are:

- Read in the data as a Pandas DataFrame
- Use .astype(str) to convert the specified columns to strings
- Leave var4 and var5 as numeric (default Pandas behavior) 
- Save the updated DataFrame to a new object