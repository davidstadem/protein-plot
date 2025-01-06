from dash import dcc, html, Dash
from dash.dependencies import Input, Output
import plotly.graph_objects as go

import make_protein_plot as mp

app = Dash(__name__)


@app.callback(
    Output('contour-plot', 'figure'),
)
def update_graph():
    
    import numpy as np
    x=np.random.random(100)
    y=np.random.random(100)
    fig = go.Figure(data=[go.Scatter(x=x, y=y, mode='markers')]) #Invisible trace to prevent empty plot on initial load

    df,fig = mp.make_fig_easy()
    return fig

fig = update_graph()

def readme():
    with open('README.md', 'r') as file:
        content = file.read()
    return content

markdown_text = readme()

app.layout = html.Div([
    #    #dcc.Graph(id='contour-plot'),
    html.Div(  # Container for the graph
        dcc.Graph(
            id='protein-plot', 
            figure=fig,
            responsive=True, 
            style={'height': '100%',}, #Important for resizing
        ),
        style={
            'width': '80%',  # Adjust as needed
            'margin': 'auto',
            'aspectRatio': '16/9', #Or any other desired aspect ratio like 16/9, 4/3, etc.
        }
    ),
    dcc.Markdown(children=markdown_text),  
])

if __name__ == '__main__':
    app.run_server(debug=True)