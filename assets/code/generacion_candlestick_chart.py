# --- DATASET ---
# https://www.kaggle.com/datasets/umerhaddii/google-stock-data-2024


import plotly.graph_objects as go
import pandas as pd
import os

df = pd.read_csv('GOOG_2004-08-19_2025-08-20.csv')

fig = go.Figure(data=[go.Candlestick(x=df['date'],s
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'])])

# Guardar la figura como una imagen PNG
fig.write_image("google_stock_candlestick.png")

fig.show()