import pandas as pd
import math

# Read CSV file
df = pd.read_csv('online-retail.csv')

# Deleting zero values

df = df.drop(df[df['UnitPrice'] == 0].index)
df = df.drop(df[df['Quantity'] == 0].index)

negative_array = df[df['UnitPrice'] < 0].index.to_numpy()
positive_array = df[df['UnitPrice'] > 0].index.to_numpy()



## Print tests

print(df.info())
x = df.loc[[299983]]
print(x)
print(negative_array)



## Note iloc is for the actual row in the table loc is the one you can see ##