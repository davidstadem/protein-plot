from dash import dcc, html, Dash, Input, Output, callback
import plotly.graph_objects as go

import protein_plot

proteinplot = protein_plot.ProteinPlot()

app = Dash(__name__)

csv_string=''

@callback(
    Output('contour-plot', 'figure'),
    Input('protein-plot', 'csvpath'),
)
def update_graph(csvpath):
    if csvpath is None:
        csvpath = protein_plot.PRICESPATH
    proteinplot.read_df(csvpath)
    proteinplot.clean_df()
    proteinplot.make_plot()
    fig=proteinplot.add_contour(y_range=(0,11.5))
    return fig

@callback(
    Output("download-dataframe-csv", "data"),
    Input("download-csv", "n_clicks"),
    prevent_initial_call=True,
)
def download_csv(n_clicks):
    df = proteinplot.df
    return dcc.send_data_frame(df.to_csv, "proteinplot.csv")

fig = update_graph(csvpath=protein_plot.PRICESPATH)

def readme():
    with open('README.md', 'r') as file:
        content = file.read()
    return content

markdown_text = readme()

app.layout = html.Div([
    html.Div(
        dcc.Graph(
            id='protein-plot', 
            figure=fig,
            responsive=True, 
            style={'height': '100%',},
        ),
        style={
            'width': '80%', 
            'margin': 'auto',
            'aspectRatio': '16/9', 
        },
    ),
    html.Button("Download CSV!", id="download-csv"),
    dcc.Download(id="download-dataframe-csv"),
    dcc.Markdown(children=markdown_text),  
])

if __name__ == '__main__':
    app.run_server(debug=True)