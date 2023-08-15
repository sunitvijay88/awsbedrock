import pandas as pd
import seaborn as sns

sepallength = 'Sepal Length in mm.'       
sepalwidth = 'Sepal Width in mm.'              
petallength = 'Petal Length in mm.'        
petalwidth = 'Petal Width in mm.'

data = """50 33 14 02       
46 34 14 03  
46 36 .  02"""

setosa_df = pd.read_csv(data, delimiter=' ', header=None)
setosa_df.columns = [sepallength, sepalwidth, petallength, petalwidth]

corr = setosa_df.corr()

print(corr)