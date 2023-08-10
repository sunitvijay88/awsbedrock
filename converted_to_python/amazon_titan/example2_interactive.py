# Import the necessary libraries
import sas7bdat
data = sas7bdat("your_file_path", input=["var1", "var2", "var3", "var4", "var5"], keepnames=True)  
# Convert the selected variables to strings
data.var1 = data.var1.str.upper()
data.var2 = data.var2.str.upper()
data.var3 = data.var3.str.upper()
# Keep var4 and var5 as numeric
data.var4 = float(data.var4)
data.var5 = float(data.var5)
print(data)