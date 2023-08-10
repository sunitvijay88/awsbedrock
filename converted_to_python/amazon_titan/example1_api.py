import pandas as pd 
# for data processing
import matplotlib.pyplot as plt 
# for plotting the data
data = pd.read_csv(\"data.csv\", header=0, index_col=0)
# converts the column names into data frame column names
data.columns = [\"Sepal Length\",\"Sepal Width\",\"Petal Length\",\"Petal Width\" ]
# creates a data frame from the given SAS code data
df = data.copy()
# adds new column with the label names as string
df.insert(2, \"sepallength\", data.Sepal Length.astype(str))
df.insert(3, \"sepalwidth\", data.Sepal Width.astype(str))
df.insert(4, \"petallength\", data.Petal Length.astype(str))
df.insert(5, \"petalwidth\", data.Petal Width.astype(str))
# plots the data frame
plt.scatter(df.sepallength, df.sepalwidth, s=df.petallength*1.5, c=df.petalwidth*1.5, label=\"Fisher (1936) Iris Setosa Data\")
plt.xlabel(\"Sepal Length (mm)\" )
plt.ylabel(\"Sepal Width (mm)\" )
plt.legend()