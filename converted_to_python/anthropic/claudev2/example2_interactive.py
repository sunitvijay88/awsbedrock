import pandas as pd

# Read in the data
df = pd.read_csv('your_file_path') 

# Convert selected columns to strings
df['var1'] = df['var1'].astype(str)  
df['var2'] = df['var2'].astype(str)
df['var3'] = df['var3'].astype(str)

# Keep var4 and var5 as numeric

# Output the reformatted data
df.to_csv('reformatted_data.csv', index=False)
```

The key steps:

- Read in the data using pandas 
- Use astype(str) to convert the numeric columns to strings
- Keep var4 and var5 as numeric (pandas will infer these as numeric)
- Write out the converted DataFrame to a new CSV file

This preserves the structure of the SAS code while using pandas functions to handle the data conversions and output.