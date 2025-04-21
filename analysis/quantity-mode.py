import math

# Opening cleaning.py and reading it with read() and executing if with exec()
with open("cleaning/cleaning.py") as file:
    exec(file.read())

df1 = df[["StockCode","Description","Quantity"]]
df1 = df1.drop(df1[df1['Quantity'] < 0].index) 

# Finding mode

mode = df1['Quantity'].mode() # This shows that the most common amount of items bought per product is one.


## Print tests

print(mode)