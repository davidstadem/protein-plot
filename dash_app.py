from dash import dcc, html, Dash, Input, Output, State, callback
import io
import base64
import protein_plot

proteinplot = protein_plot.ProteinPlot()
# Add external stylesheets to your Dash app
external_stylesheets = ['/assets/style.css'] # Link to your CSS file
app = Dash(__name__, external_stylesheets=external_stylesheets) # Initialize Dash app with stylesheets

def plot_from_strio(strio=None):
    if strio is None:
        strio = protein_plot.PRICESPATH
    proteinplot.read_df(strio)
    proteinplot.clean_df()
    proteinplot.make_plot()
    fig=proteinplot.add_contour(y_range=(0,11.5))
    return fig

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

def markdown_text(filepath):
    with open(filepath, 'r') as file:
        content = file.read()
    return content

app.layout = html.Div([
    dcc.Markdown(children='# The Protein Plot\nHi, this is the protein plot.'),
    html.Div(
        dcc.Graph(
            id='protein-plot',
            responsive=True,
            style={'height': '100%',},
        ),
        style={
            'width': '80%',
            'margin': 'auto',
            'aspectRatio': '16/9',
        },
    ),
    # Container for side-by-side buttons
    html.Div([
        # Download button first for left positioning
        html.Button(
            "Download this plot as a CSV file.",
            id="download-csv",
            className='material-button', # Apply the 'material-button' class
        ),
        dcc.Upload(
            id='upload-data',
            # Apply 'material-button' class to the clickable child of dcc.Upload
            children=html.Div(
                ['Upload your own file: ', html.A('Select a CSV File', className='upload-button-link')],
                className='material-button' # This div acts as the clickable button part
            ),
            # Apply 'dcc-upload-container' to the dcc.Upload component itself
            className='dcc-upload-container',
            multiple=False,
        ),
    ], style={'display': 'flex', 'justifyContent': 'center', 'margin': '10px 0'}), # Flexbox for side-by-side
    dcc.Download(
        id="download-dataframe-csv",
    ),
    html.Img(
        src='static/excaliprotein.png',
        style={'width': '50%', 'display': 'block', 'margin': 'auto', 'padding': '20px 0'},
    ),
    dcc.Markdown(children=markdown_text('quickstart.md'),mathjax=True),
    html.Img(
        src='static/protein-plot.png',
        style={'width': '100%',},
    ),
    dcc.Markdown(children=markdown_text('manifesto.md'),mathjax=True),
])

if __name__ == '__main__':
    app.run_server(debug=True)