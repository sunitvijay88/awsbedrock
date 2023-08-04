import pandas as pd

data = pd.read_csv('Setosa.csv', index_col=None, header=None)

data['Sepal Length in mm.'] = data['Sepal Length']
data['Sepal Width in mm.'] = data['Sepal Width']
data['Petal Length in mm.'] = data['Petal Length']
data['Petal Width in mm.'] = data['Petal Width']

data.columns = ['Sepal Length in mm.', 'Sepal Width in mm.', 'Petal Length in mm.', 'Petal Width in mm.']

data.head()