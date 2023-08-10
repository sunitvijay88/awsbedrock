# imports the necessary libraries
import os
import sys
from datetime import datetime
import pandas as pd
import numpy as np
# defines the function that generates the regression models
def generate_regression_models(input_files):
    # defines a list of regression models
    models = []
    # iterates over the input files
    for input_file in input_files:
        # reads the CSV file and stores the data in a Pandas DataFrame
        data = pd.read_csv(input_file, delimiter="", header=0)
        # removes the first observation since it is the header
        data = data.drop(data.index[0], axis=1)
        # converts the data into a numpy array
        x = np.array(data.iloc[:, 1:])
        y = np.array(data.iloc[:, 0])
        # fits a linear regression model to the data
        try:
            model = np.linalg.lstsq(x, y)[0]
        except:
            print("Unable to fit a linear regression model")
        # creates a regression model object and stores it in the list of models
        models.append(RegressionModel(input_file, model))
    # prints a message indicating that all regression models have been generated
    print("All regression models have been generated successfully")
    return models
# class that represents a regression model
class RegressionModel:
    def __init__(self, input_file, model):
        # stores the input file name
        self.input_file = input_file
        # stores the linear regression model
        self.model = model
        # creates a datetime object with the current date and time
        self.creation_date = datetime.now()
    # returns the name of the input file
    def get_input_file_name(self):
        return self.input_file
    # returns the linear regression model
    def get_model(self):
        return self.model
    # returns a datetime object representing the creation date of the regression model
    def get_creation_date(self):
        return self.creation_date
# function that reads the CSV file and stores the data in a Pandas DataFrame
def read_csv_file(file_path):
    data = pd.DataFrame()
    # opens the CSV file
    with open(file_path) as csv_file:
        # defines a reader object that iterates over the lines of the CSV file
        csv_reader = csv.reader(csv_file, delimiter="",skipinitialspace=True)
        for row in csv_reader:
            # adds the row to the Pandas DataFrame
            data = data.append(row, ignore_index=True)
    return data
if __name__ == "__main__":
    # reads the list of input files from the command-line argument
    input_files = sys.argv[1:]
    # generates the regression models
    models = generate_regression_models(input_files)
    # prints the list of regression models
    for model in models:
        print(model)