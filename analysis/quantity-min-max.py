import pandas as pd
import math

# Read CSV file
df = pd.read_csv('online-retail.csv')

# Finding minimum and maximum values

minimum = df['Quantity'].min()    # Minimum and maximum are opposites of each other suggesting that these transactions are refunds. 
maximum = df['Quantity'].max()    # To find the true minimum and maximum we must find the smallest positive integer and the maximum should not have a negative quivalent.


id_minimum = df['Quantity'].idxmin()
id_maximum = df['Quantity'].idxmax()

# Find information of refunded rows

print(df.loc[[id_minimum]])   # After analysing these results we can see that the transaction is a refund 
print(df.loc[[id_maximum]])

# Removing refunded rows

a = id_minimum
b = id_maximum

df = df.drop([a,b])

# Drop check


true_minimum = df['Quantity'].min()    # Minimum and maximum are opposites of each other suggesting that these transactions are refunds. 
true_maximum = df['Quantity'].max()

true_id_minimum = df['Quantity'].idxmin()
true_id_maximum = df['Quantity'].idxmax()


print('The ID' , true_id_minimum)
print('contain the minimum which is' , true_minimum)
print('The ID' , true_id_maximum)
print('contain the maximum which is' , true_maximum)



## Print tests

# print('The ID' , id_minimum)
# print('contain the minimum which is' , minimum)
# print('The ID' , id_maximum)
# print('contain the maximum which is' , maximum)
