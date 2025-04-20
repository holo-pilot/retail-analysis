import pandas as pd
import math

# Read CSV file
df = pd.read_csv('online-retail.csv')

# Summing quantity column

total = df['Quantity'].sum()

# Mean is total / number of rows

rows = 541909
true_mean = total / rows
mean = math.floor(true_mean)  # Mean is rounded down as quantity cannont be half of something. On average the 9 items are bought per product

# Finding mode

mode = df['Quantity'].mode() # This shows that the most common amount of items bought per product is one.

true_minimum = df['Quantity'].min()    # Minimum and maximum are opposites of each other suggesting that these transactions are refunds. 
true_maximum = df['Quantity'].max()

true_id_minimum = df['Quantity'].idxmin()
true_id_maximum = df['Quantity'].idxmax()


print('The ID' , true_id_minimum)
print('contain the minimum which is' , true_minimum)
print('The ID' , true_id_maximum)
print('contain the maximum which is' , true_maximum)

## Print tests

# print(total)
# print(true_mean)
# print(mean)
# print(mode)
