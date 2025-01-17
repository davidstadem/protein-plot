import dash
from dash import dcc, html, Dash, Input, Output, State, callback
import plotly.graph_objects as go
import io
import base64
import protein_plot

proteinplot = protein_plot.ProteinPlot()

def plot_from_strio(strio=None):
    if strio is None:
        strio = protein_plot.PRICESPATH
    proteinplot.read_df(strio)
    proteinplot.clean_df()
    proteinplot.make_plot()
    fig=proteinplot.add_contour(y_range=(0,11.5))
    return fig

app = Dash(__name__)

csv_string=''

def contents_to_stringIO(contents):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    utf8io = io.StringIO(decoded.decode('utf-8'))
    return utf8io

error_dict = {
    "data": [],
    "layout": {
        "title": None,
    }
}


@callback(
    Output('protein-plot', 'figure'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename'),
)
def update_graph(contents, filename):
    if contents is None:
        fig = plot_from_strio(None)
        return fig
    else:
        strio = contents_to_stringIO(contents)

        if isinstance(strio, io.StringIO):
            try:
                fig = plot_from_strio(strio)
                return fig
            except Exception as e:
                rdict = error_dict
                rdict['layout']['title'] = f"Error generating plot: {e}"
                return rdict
        else:
            rdict = error_dict
            rdict['layout']['title'] = "Error processing uploaded file"
            return rdict

@callback(
    Output("download-dataframe-csv", "data"),
    Input("download-csv", "n_clicks"),
    prevent_initial_call=True,
)
def download_csv(n_clicks):
    df = proteinplot.df
    return dcc.send_data_frame(df.to_csv, "proteinplot.csv")

#fig = update_graph(csvpath=protein_plot.PRICESPATH)

def readme():
    with open('README.md', 'r') as file:
        content = file.read()
    return content

markdown_text = readme()

app.layout = html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div(['Drag and Drop or ', html.A('Select Files')]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        multiple=False  # Allow only one file to be uploaded
    ),
    html.Div(
        dcc.Graph(
            id='protein-plot', 
            #figure=fig,
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