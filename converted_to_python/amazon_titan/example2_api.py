You can convert the SAS code to Python using the Pandas library as shown in the code. The Pandas library is a powerful data analysis tool for Python that allows you to read, write, manipulate, and analyze data. 
Import the Pandas library:
```
import pandas as pd
```
Read in the data:
```
df = pd.read_csv('your_file_path')
```
Convert selected variables to strings:
```
df['var1'] = df['var1'].astype(str)
df['var2'] = df['var2'].astype(str)
df['var3'] = df['var3'].astype(str)
```
```
# Output the reformatted data
df.to_csv('reformatted_data.csv', index=False)
```
This code assumes that the data in your file is comma-separated. If your data is in a different format, you will need to modify the code accordingly. Also, make sure that you have the Pandas library installed before running the code.