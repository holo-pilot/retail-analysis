import pandas as pd

# Read CSV file
df = pd.read_csv('online-retail.csv')

# Print first 10 rows



# Print data information

print(df.info())

# Null values check

empty_columns = df.isnull().all(axis=0)
print(empty_columns)

# Find duplicates

duplicates = df[df.duplicated(['InvoiceNo', 'StockCode','CustomerID','Description','InvoiceDate'], keep=False)]
print(duplicates)

