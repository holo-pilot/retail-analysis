import pandas as pd

# Read the xlsx file 

df = pd.read_excel('Online Retail.xlsx', sheet_name='Online Retail',header=0)

# Write the DataFrame to a CSV file with the to_csv() function

df.to_csv('online-retail.csv',index=0)
