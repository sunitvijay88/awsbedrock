def generate_regression_models(input_files):
    # Split input files into list
    input_files = input_files.split() 
    
    for i, input_file in enumerate(input_files):
        # Read data from input file into DataFrame
        import pandas as pd
        data = pd.read_csv(input_file, delimiter=',', skiprows=1)
        
        # Fit linear regression model
        from sklearn.linear_model import LinearRegression
        model = LinearRegression().fit(data[['x']], data['y'])
        
        print(f"Linear regression model for {input_file} has been generated")
        
    print("All regression models have been generated successfully")
```

generate_regression_models("path/to/file1.csv path/to/file2.csv path/to/file3.csv")
