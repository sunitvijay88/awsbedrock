import numpy as np
from sklearn.datasets import make_regression
from sklearn.externals import joblib

# Set random seed
np.random.seed(0)

# Generate synthetic data
X, y = make_regression(n_samples=100, n_features=10, noise=0.5, random_state=0)

# Save in csv format
with open("data/synthetic_regression.csv", "w") as f:
    f.write("target, feature\\_1, feature\\_2, feature\\_3, feature\\_4, feature\\_5, feature\\_6, feature\\_7, feature\\_8, feature\\_9, feature\\_10\n")
    for i, instance in enumerate(X):
        f.write(f"{y[i]}, {instance[0]}, {instance[1]}, {instance[2]}, {instance[3]}, {instance[4]}, {instance[5]}, {instance[6]}, {instance[7]}, {instance[8]}, {instance[9]}\n")

# Save the model for later use if needed
joblib.dump(X, "data/synthetic_regression.model")


This script uses the scikit-learn`make_regression`function to generate the data and then the`joblib`library to save the model for later use if needed.