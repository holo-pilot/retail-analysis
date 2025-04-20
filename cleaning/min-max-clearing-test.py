import pandas as pd
import math

# Read CSV file
df = pd.read_csv('online-retail.csv')


while True:

    minimum = df['Quantity'].min() 
    maximum = df['Quantity'].max()

    if minimum + maximum == 0:
        
        id_minimum = df['Quantity'].idxmin()
        id_maximum = df['Quantity'].idxmax()
        df = df.drop([id_minimum,id_maximum])

    else:
        
        a = id_minimum
        b = id_maximum
        break


id_minimum = df['Quantity'].idxmin()
id_maximum = df['Quantity'].idxmax()

# print(df.loc[[id_minimum]])    
# print(df.loc[[id_maximum]])

# x = df.loc[[225529]]
# print(x)



negative_array = df[df['Quantity'] < 0].index.to_numpy()

# negative_array = df[df['StockCode'] == '23005' ].index.to_numpy()

print(negative_array)
x = df.loc[[541717]]
print(x)









