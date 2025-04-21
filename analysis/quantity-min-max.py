
# Opening cleaning.py and reading it with read() and executing if with exec()
with open("cleaning/cleaning.py") as file:
    exec(file.read())


df = df[["StockCode","Description","Quantity"]]
df = df.groupby('StockCode').sum()
df = df.drop(df[df['Quantity'] <= 0].index)     # Values with negative quantities are dropped as it is assumed that they are negative due to inventory error. Zeros are assumed the same.

print(df.info())

minimum = df['Quantity'].min()    # Minimum and maximum are opposites of each other suggesting that these transactions are refunds. 
maximum = df['Quantity'].max()    # To find the true minimum and maximum we must find the smallest positive integer and the maximum should not have a negative quivalent.


id_minimum = df['Quantity'].idxmin()
id_maximum = df['Quantity'].idxmax()

# Find information of refunded rows

print(df.loc[[id_minimum]])   
print(df.loc[[id_maximum]])




## Note iloc is for the actual row in the table loc is the one you can see ##