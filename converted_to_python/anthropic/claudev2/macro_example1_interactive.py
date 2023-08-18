import os
from sas7bdat import SAS7BDAT
import pandas as pd
from sklearn.linear_model import LinearRegression

def generate_regression_models(input_files):
  
  for i, input_file in enumerate(input_files):
    
    # Read CSV data into Pandas DataFrame
    data = pd.read_csv(input_file)
    
    # Fit linear regression model
    reg = LinearRegression().fit(data['x'].values.reshape(-1,1), data['y'])
    
    # Save model coefficients
    output_file = f'outest{i+1}.csv'
    pd.DataFrame(reg.coef_, columns=['coefficient']).to_csv(output_file)
    
    print(f'Linear regression model for {input_file} has been generated')
    
  print('All regression models have been generated successfully')

input_files = ['path/to/file1.csv', 'path/to/file2.csv', 'path/to/file3.csv']
generate_regression_models(input_files)
```

The main steps are:

- Loop through each input CSV file 
- Read into Pandas DataFrame
- Fit linear regression model using sklearn
- Save model coefficients to a CSV file
- Print logging statements like in SAS macro

This implements the same functionality as the SAS macro to generate a separate linear regression model for each CSV data file provided.