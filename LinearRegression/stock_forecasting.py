import pandas as pd
import quandl

# Get Data frame from quadl
df = quandl.get('WIKI/GOOGL')

# Relation between High and Low features show volatility during the day
# Open - Close determines if the price went up or down and how much
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]

# High-Low porcentage, represents the volatility
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0

# Daily porcent change
df['PCT_Change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

# Just keeping meaningful data features
df = df[['Adj. Close', 'HL_PCT', 'PCT_Change', 'Adj. Volume']]

print (df.head())