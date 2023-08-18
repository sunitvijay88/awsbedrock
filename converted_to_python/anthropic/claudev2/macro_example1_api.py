import pandas as pd
from sklearn.linear_model import LinearRegression

def generate_regression_models(input_files):
    for i, input_file in enumerate(input_files):
        
        # Read CSV file into Pandas DataFrame
        df = pd.read_csv(input_file, sep=',') 

        # Extract X and y 
        y = df['y']
        X = df['x'].values.reshape(-1,1)

        # Fit linear regression model
        model = LinearRegression()
        model.fit(X, y)

        # Export model coefficients
        coeff_df = pd.DataFrame(model.coef_, columns=['coef'])
        coeff_df.to_csv(f'outest{i+1}.csv')
        
        print(f'Linear regression model for {input_file} has been generated')

    print('All regression models have been generated successfully')

input_files = ['file1.csv', 'file2.csv', 'file3.csv']
generate_regression_models(input_files)
```

The key steps are:

1. Read CSV file into Pandas DataFrame
2. Extract X and y columns 
3. Fit linear regression model using scikit-learn 
4. Export model coefficients to a CSV file
5. Print confirmation message for each model


- No need for explicit data step, just read CSV directly into DataFrame
- Fit model using scikit-learn instead of SAS PROC REG
- Export coefficients to CSV instead of SAS OUTEST dataset
- Use Python print() instead of SAS %PUT statement
- Loop over files using Python for loop instead of SAS %DO loop