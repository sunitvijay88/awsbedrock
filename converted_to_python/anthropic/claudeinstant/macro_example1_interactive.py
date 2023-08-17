import pandas as pd

def generate_regression_models(input_files):
    for input_file in input_files.split():  
        mydata = pd.read_csv(input_file, delimiter=',', skiprows=1, names=['x', 'y'])
        
        from sklearn.linear_model import LinearRegression
        model = LinearRegression()
        model.fit(mydata[['x']], mydata['y'])
        
        print(f"Linear regression model for {input_file} has been generated")
        
    print("All regression models have been generated successfully")
        
input_files = "path/to/file1.csv path/to/file2.csv path/to/file3.csv"
generate_regression_models(input_files)

This does the following:

- Splits the input files string into a list
- Reads each CSV file into a DataFrame using Pandas
- Fits a linear regression model using scikit-learn     
- Prints a message to indicate the model has been generated
- Finally prints a success message
