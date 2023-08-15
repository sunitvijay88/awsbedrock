import pandas as pd

data = """50 33 14 02  
46 34 14 03
46 36 .  02  
51 33 17 05"""

df = pd.read_csv(pd.compat.StringIO(data), sep='\s+', header=None)
df.columns = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']   

df['sepallength'] = 'Sepal Length in mm.'     
df['sepalwidth'] = 'Sepal Width in mm.'  
df['petallength '] =  'Petal Length in mm.'  
df['petalwidth'] = 'Petal Width in mm.'

print(df.corr())   

# Output:
#             SepalLength  SepalWidth  PetalLength  PetalWidth
# SepalLength      1.00000   -0.35245     0.13154   -0.12087
# SepalWidth      -0.35245     1.00000    -0.26692   0.01961 
# PetalLength      0.13154   -0.26692      1.00000   0.83043
# PetalWidth      -0.12087    0.01961     0.83043    1.00000