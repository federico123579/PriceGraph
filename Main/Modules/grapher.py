import pandas as pd
import plotly.graph_objs as go
import plotly.plotly as py
from library import library
def linear_graph(link_to_file):
    py.sign_in('federico123579', 'tmp58hnp2w')
    # Import data from csv
    df = pd.read_csv(link_to_file)
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
    py.plot(fig, filename='price-date-csv')
def box_plot(data_array):
    data = [
        go.Box(
            y = data_array,
            boxpoints = 'all',
            jitter = 0.3,
            pointpos = -1.8,
            name = "Battlefield 1",
            marker = dict(
                color = 'rgb(0, 128, 128)',
            )
        )
    ]
    py.plot(data, filename='pirce-average-box-plot')
if __name__ == '__main__':
    path = raw_input("insert Path: ")
    linear_graph(path)
