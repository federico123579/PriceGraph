import pandas as pd
import plotly.graph_objs as go
import plotly.plotly as py
from library import library
def send_to_make_graph():
    py.sign_in('federico123579', 'tmp58hnp2w')
    # Import data from csv
    df = pd.read_csv('data.txt')
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
if __name__ == '__main__':
    send_to_make_graph()
