import pandas as pd


# Read CSV file

df = pd.read_csv('online-retail.csv')

# Cleaning

df = df.drop(df[df['UnitPrice'] == 0].index)
df = df.drop(df[df['Quantity'] == 0].index)
df = df.drop(df[df['StockCode'] == "S"].index)
df = df.drop(df[df['StockCode'] == "POST"].index)
df = df.drop(df[df['StockCode'] == "D"].index)
df = df.drop(df[df['StockCode'] == "AMAZONFEE"].index)