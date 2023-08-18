import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

df = pd.read_csv('iris_setosa.csv') 

df.columns = ['SepalLength','SepalWidth','PetalLength','PetalWidth']

df['SepalLength'] = df['SepalLength'].astype(float)
df['SepalWidth'] = df['SepalWidth'].astype(float) 
df['PetalLength'] = df['PetalLength'].astype(float)
df['PetalWidth'] = df['PetalWidth'].astype(float)

print(df.dtypes)

print(df.corr())

scatter_matrix(df, figsize=(10, 8))
plt.suptitle("Fisher's Iris Setosa Data", y=1.05)
plt.show()
```

The key steps are:

- Read CSV data into a pandas DataFrame
- Rename columns to match SAS code 
- Convert columns to float data types
- Calculate correlations using df.corr()
- Generate scatter plot matrix visualizing correlations

This generates the correlation matrix and scatter plot matrix to match the SAS output.