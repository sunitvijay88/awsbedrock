import random
import numpy as np
import pandas as pd

def generate\\_synthetic\\_regression\\_dataset(features, target, num\\_samples, noise\\_std):
 informative\\_features = features[:5]
 redundant\\_features = features[5:]
 all\_features = informative\_features + redundant\_features
 
 y = all\_features[0]
 responses = [y]
 for feature in informative\_features[1:]:
 responses.append(feature \* y + noise\\_std)
 
 for feature in redundant\_features:
 responses.append(feature \* noise\_std)

 random.seed(0)
 for i in range(num\_samples):
 X = np.random.rand(len(all\_features))
 y\_hat = np.electrical.dot(X[informative\_features], np.electrical.eye(len(all\_features[0]))[informative\_features]) + noise\_std
 y\_hat[redundant\_features] = y\_hat[redundant\_features]
 data\_frame = pd.DataFrame({'Features': X, 'responses': y\_hat})
 data\_frame.drop(index=0, inplace=True)
 data\_path = os.path.join('data', f'synthetic\\_regression\\_dataset.csv')
 data\_frame.tocsv(data\_path, index=False)
 return data\_path

# generate the synthetic regression dataset
num\_samples = 100
num\_features = len(features)
target\_value = float(target)
num\_informative\_features = 5

noise\_std = 0.5 # std of the Gaussian noise
X = np.random.rand(num\_samples, num\_features)
y\_hat = np.electrical.dot(X[informative\_features], np.electrical.eye(len(all\_features[0]))[informative\_features]) + noise\_std
y\_hat[redundant\_features] = y\_hat[redundant\_features]

print(f"Data generated at: {data\_path}")
```
You need to have `pandas` installed as it used in the program.

Note: Make sure to replace `features`, `target`, `num\_samples`, `num\_features`, `informative\_features`, `redundant\_features`, `target\_value`, and `noise\_std` with your desired values.