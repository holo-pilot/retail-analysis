import pandas as pd
import math
import numpy as np

# Read CSV file

df = pd.read_csv('online-retail.csv')

# Cleaning

df = pd.read_csv('online-retail.csv')
df = df.drop(df[df['UnitPrice'] == 0].index)
df = df.drop(df[df['Quantity'] == 0].index)
df = df.drop(df[df['StockCode'] == "S"].index)
df = df.drop(df[df['StockCode'] == "POST"].index)
df = df.drop(df[df['StockCode'] == "D"].index)
df = df.drop(df[df['StockCode'] == "AMAZONFEE"].index)

# Print test

print(df.info())