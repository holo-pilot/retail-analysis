# Opening cleaning.py and reading it with read() and executing if with exec()
with open("cleaning/cleaning.py") as file:
    exec(file.read())

df = df.drop(df[df['Quantity'] < 0].index) 

# Summing of column
## Using exception in case column has mixed data types

try:
    total = df['UnitPrice'].sum()
    print(total)
except Exception as e:
    print(e)
  

## total = df['UnitPrice'].sum() Use if confident there is no mixed or null data

## total = df['UnitPrice'].sum(skipna=True) if there were missing values

# Print total

# print(total)

## All test show 2498803.974 suggesting data is clean