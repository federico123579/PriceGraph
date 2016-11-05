import pandas as pd
import plotly.graph_objs as go
import plotly.plotly as py
py.sign_in('federico123579', 'tmp58hnp2w')
# Import data from csv
df = pd.read_csv('data.txt')
print(df.head())
trace1 = go.Scatter(
    x = df['Date'],
    y = df['Battlefield 1'],
    mode = 'lines+markers',
    name = 'Battlefield 1'
)
trace2 = go.Scatter(
    x = df['Date'],
    y = df['Battlefront: Season Pass'],
    mode = 'lines+markers',
    name = 'Battlefront: Season Pass'
)

layout = go.Layout(title='Price of Instant Gaming')

fig = go.Figure(data=[trace1, trace2], layout=layout)

# Plot data in the notebook
py.iplot(fig, filename='price-date-csv')
