from dash import dcc, html, Dash, Input, Output, callback
import plotly.graph_objects as go

import protein_plot as mp

app = Dash(__name__)

csv_string=''

@callback(
    Output('contour-plot', 'figure'),
    Input('protein-plot', 'relayoutData'),
)
def update_graph():
    
    import numpy as np
    x=np.random.random(100)
    y=np.random.random(100)
    fig = go.Figure(data=[go.Scatter(x=x, y=y, mode='markers')]) #Invisible trace to prevent empty plot on initial load

    df,fig = mp.make_fig_easy()
    global csv_string
    csv_string = df.to_csv(index=False, encoding='utf-8')
    return fig

@callback(
    Output("download-dataframe-csv", "data"),
    Input("download-csv", "n_clicks"),
    prevent_initial_call=True,
)
def download_csv(n_clicks):
    import pandas as pd
    df=pd.DataFrame([0,4,2,5])
    return dcc.send_data_frame(df.to_csv, "mydataset.csv") #Much simpler and more efficient

    #return dict(content="Hello world!", filename="hello.txt")

    #return dict(content=csv_string, filename="mydataset.csv")


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
    html.Button("Download CSV Me!", id="download-csv"),
    dcc.Download(id="download-dataframe-csv"),
    dcc.Markdown(children=markdown_text),  
])

if __name__ == '__main__':
    app.run_server(debug=True)