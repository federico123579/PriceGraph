import pandas as pd
import plotly.graph_objs as go
import plotly.plotly as py
import sys
sys.path.insert(0, 'Modules')
from library import library
py.sign_in('federico123579', 'tmp58hnp2w')
# Import data from csv
df = pd.read_csv('data.txt')
print(df.head())
data = []
for count in range(len(library)):
    data.append(go.Scatter(
        x = df['Date'],
        y = df[library[count]['name']],
        mode = 'lines+markers',
        name = library[count]['name']
    ))
layout = go.Layout(title='Price of Instant Gaming')
fig = go.Figure(data=data, layout=layout)

# Plot data in the notebook
py.iplot(fig, filename='price-date-csv')
