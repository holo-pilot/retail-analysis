import pandas as pd
import math
import numpy as np




# opening cleaning.py and reading it with read() and executing if with exec()
with open("cleaning/cleaning.py") as file:
    exec(file.read())



df1 = df[["StockCode","Description","Quantity"]]
df1 = df1.drop(df1[df1['Quantity'] < 0].index)     # Values with negative quantities are dropped as it is assumed that they are negative due to inventory error.
df1 = df1.groupby('StockCode').sum()


print(df1.info())

minimum = df1['Quantity'].min()    # Minimum and maximum are opposites of each other suggesting that these transactions are refunds. 
maximum = df1['Quantity'].max()    # To find the true minimum and maximum we must find the smallest positive integer and the maximum should not have a negative quivalent.


id_minimum = df1['Quantity'].idxmin()
id_maximum = df1['Quantity'].idxmax()

# Find information of refunded rows

print(df1.loc[[id_minimum]])   
print(df1.loc[[id_maximum]])






## Note iloc is for the actual row in the table loc is the one you can see ##