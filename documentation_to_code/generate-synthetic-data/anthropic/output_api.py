import numpy as np
import pandas as pd

np.random.seed(0)

n = 100
p = 10
p_informative = 5

# Generate coefficients
coef = np.random.rand(p_informative)

# Generate feature matrix
X = np.random.rand(n, p)

# Generate y based on informative features  
y = np.dot(X[:,0:p_informative], coef)

# Add noise
y += np.random.normal(0, 0.5, size=n)

# Assemble dataset 
df = pd.DataFrame(X)
df['y'] = y

# Save to CSV
import os
os.makedirs('data', exist_ok=True)
df.to_csv('data/synthetic_regression.csv', index=False)

print("Dataset saved to data/synthetic_regression.csv")