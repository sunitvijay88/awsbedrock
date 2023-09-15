import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_regression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from random import seed
from os.path import dirname, join
try:
    seed(0)
    # Generate the informative features
    informative_features = np.random.randint(2, 10, 5)
    X = np.random.randint(2, 10, (100, informative_features))
    y = X[:, 0] + X[:, 1] * 0.1 + X[:, 2] * 0.2 + X[:, 3] * 0.3 + X[:, 4] * 0.4
    # Generate the redundant features
    redundant_features = np.random.randint(2, 10, 5)
    X_redundant = np.random.randint(2, 10, (100, redundant_features))
    X = np.concatenate((X, X_redundant), axis=1)
    # Generate the linear model coefficients
    beta = np.random.rand(informative_features)
    # Generate the noise
    noise = np.random.normal(0, 0.5, (100, informative_features))
    y += np.dot(beta, X) + noise
    # Scale the data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.25)
    # Fit the linear model
    lin_reg = LinearRegression().fit(X_train, y_train)
    # Generate the random forest model
    rf_reg = RandomForestRegressor(n_estimators=100).fit(X_scaled, y)
    # Save the data to a CSV file
    df = pd.DataFrame(X_scaled, columns=["feature%d" % i for i in range(informative_features + redundant_features)])
    df["target"] = y
    df.to_csv(join(dirname(__file__), "data", "synthetic_regression.csv"))
    # Print the intercept and slope of the linear model
    print("Intercept:", lin_reg.intercept_)
    print("Slope:", lin_reg.coef_[0])
except Exception as e:
    print("An error occurred:", str(e))
>>>Intercept: -0.25167528701883065
>>>Slope: 0.39661810052409073