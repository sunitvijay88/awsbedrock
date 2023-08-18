import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import seaborn as sns

# Read in the Iris data
df = pd.read_csv('iris.data', header=None, names=['sepal_length','sepal_width','petal_length','petal_width','species']) 

# Filter to just Setosa
setosa = df[df['species'] == 'Iris-setosa']

# Calculate correlations
corr_matrix = setosa.corr()
print(corr_matrix)

# Plot correlations
sns.heatmap(corr_matrix, annot=True)
plt.title('Correlations for Setosa Measurements')
plt.show()

# Scatterplots
sns.pairplot(setosa, kind='scatter', diag_kind='kde')
plt.suptitle('Setosa Measurements')
plt.show()