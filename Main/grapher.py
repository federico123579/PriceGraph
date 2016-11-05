import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.plotly as py
py.sign_in('federico123579', 'tmp58hnp2w')
# Import data from csv
df = pd.read_csv('data.txt')
print(df.head())
trace1 = go.Scatter(
                    x=df['Date'], y=df['Price'], # Data
                    mode='lines', name='Battlefield 1' # Additional options
                   )

layout = go.Layout(title='Price of Battlefield 1',
                   plot_bgcolor='rgb(230, 230,230)')

fig = go.Figure(data=[trace1], layout=layout)

# Plot data in the notebook
py.iplot(fig, filename='price-date-csv')
