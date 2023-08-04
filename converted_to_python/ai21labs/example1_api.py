import pandas as pd

data = pd.read_csv('Setosa.csv', index_col=None)

data['Sepal Length in mm.'] = data['Sepal Length']
data['Sepal Width in mm.'] = data['Sepal Width']
data['Petal Length in mm.'] = data['Petal Length']
data['Petal Width in mm.'] = data['Petal Width']

data.set_index('Label', inplace=True)
data.plot(kind='scatter', x='Sepal Length in mm.', y='Sepal Width in mm.', s=50, c='Petal Length in mm.', \n          marker='Petal Width in mm.')
plt.title('Fisher (1936) Iris Setosa Data')
plt.show()