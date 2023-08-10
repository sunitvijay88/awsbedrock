import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('{URL-1}', header=0)

data.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
# Drop the label column
data.drop('label', axis=1, inplace=True)

# Plot the correlation matrix
corr = data.corr()
plt.matshow(corr)
plt.yticks(range(1, 13), corr.columns)
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')

# Add a title to the plot
 
plt.title('Fisher (1936) Iris Setosa Data')
plt.show()