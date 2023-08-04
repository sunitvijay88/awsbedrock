import glob
import pandas as pd
import statsmodels.api as sm

def generate_regression_models(input_files):
    for i, input_file in enumerate(glob.glob(input_files)):
        df = pd.read_csv(input_file, header=None, names=['x', 'y'], skiprows=1)
        y = df['y']
        x = df['x']
        model = sm.GLM(y, x, family=sm.families.Gaussian())
        results = model.fit()
        print(f'Linear regression model for {input_file} has been generated')
        print(results.summary())
    print('All regression models have been generated successfully')

generate_regression_models(input_files='path/to/file1.csv path