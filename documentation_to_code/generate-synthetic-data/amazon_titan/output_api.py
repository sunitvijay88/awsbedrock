import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
np.random.seed(0)
# Generate informative features
informative_features = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']
redundant_features = ['feature6', 'feature7', 'feature8', 'feature9', 'feature10']
data = []
# Generate data for informative features
for _ in range(5):
    X = np.random.randn(100)
    X[:, informative_features] = np.sin(X[:, informative_features]) + np.random.normal(0, 0.2, X[:, informative_features].shape)
    y = X[:, informative_features].sum(axis=1)
    data.append([y.item(), *X[:, informative_features].tolist()])
# Generate data for redundant features
for _ in range(5):
    X = np.random.randn(100)
    X[:, redundant_features] = np.sin(X[:, informative_features]) + np.random.normal(0, 0.1, X[:, informative_features].shape)
    y = X[:, informative_features].sum(axis=1) + np.random.normal(0, 0.1, 1)
    data.append([y.item(), *X[:, informative_features].tolist()])
# Generate target values
X = np.random.randn(100, 5)
y = (X[:, informative_features].sum(axis=1) + 0.1 * np.random.randn(100))[:, np.newaxis]
# Fit linear regression model
regression = LinearRegression()
regression.fit(X, y)
# Generate noisy data
X_noisy = X - regression.predict(X)
y_noisy = y + 0.1 * np.random.standard_normal(X_noisy.shape)
try:
    # Write data to CSV file
    with open('data/synthetic_regression.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['target', *informative_features, *redundant_features])
        for row in data:
            writer.writerow(row)  # writerow добавляет любые значения (массив или объект) в строку (массив или жестоком) как кол-во строк
    # Plot data
    X_all = np.concatenate([data[:-1], data[-1:]], axis=0)
    X_noisy = np.concatenate([data[:-1], data[-1:]], axis=0)
    y_all = np.column_stack([row[0] for row in data])
    y_noisy = np.column_stack([row[0] for row in data])  # + 0.1 * np.random.standard_normal(row.shape)
    sns.scatterplot(X_all, y_all, color='g')
    plt.plot(X_all, y_all, color='g')
    sns.scatterplot(X_noisy, y_noisy, color='b')
    plt.plot(X_noisy, y_noisy, color='b')
    plt.xlabel('informative features')
    plt.ylabel('target')
    plt.title('Synthetic regression')
    plt.savefig('Figures/synthetic_regression.png')
    plt.clf()
    plt.close()
except Exception as e:
    print(f"An error occurred: {e}")