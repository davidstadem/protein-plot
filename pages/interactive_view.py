import dash
from dash import dcc, html, Input, Output, State, callback, no_update, callback_context
import io
import base64
import os

# --- Page-Specific Dependencies & Helpers ---

# Attempt to import protein_plot, handle if not found for basic structure.
# This logic is moved here to be self-contained within this page's view.
try:
    import protein_plot
    proteinplot_instance = protein_plot.ProteinPlot()
    PRICESPATH = protein_plot.PRICESPATH
except ImportError:
    print("Warning: protein_plot.py not found. Some features will be disabled for the interactive page.")
    proteinplot_instance = None
    PRICESPATH = None
    # Create a dummy ProteinPlot class if needed for the page to run without the file
    class DummyProteinPlot:
        def __init__(self):
            self.df = None
        def read_df(self, strio): pass
        def clean_df(self): pass
        def make_plot(self): pass
        def add_contour(self, y_range):
            return {"data": [], "layout": {"title": "Protein Plot (Data Missing)"}}
    if proteinplot_instance is None:
        proteinplot_instance = DummyProteinPlot()

# Helper function to read markdown files
def markdown_text(filepath):
    if not os.path.exists(filepath):
        default_content = f"## Placeholder for {os.path.basename(filepath)}\n\nThis is default content."
        return default_content
    try:
        with open(filepath, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading markdown file {filepath}: {e}")
        return f"Error reading {filepath}."

# Helper function to generate plot from data
def plot_from_strio(strio=None):
    if proteinplot_instance is None:
        return {"data": [], "layout": {"title": "Plotting module not loaded."}}
    
    strio_path = strio if strio is not None else PRICESPATH
    
    if strio_path is None:
        from io import StringIO
        dummy_csv = "protein,value\nProteinA,10\nProteinB,20"
        strio_path = StringIO(dummy_csv)
        print("Using dummy CSV data for initial plot as PRICESPATH is not available.")

    proteinplot_instance.read_df(strio_path)
    proteinplot_instance.clean_df()
    proteinplot_instance.make_plot()
    fig = proteinplot_instance.add_contour(y_range=(0, 11.5))
    return fig

# Helper function to process uploaded file
def contents_to_stringIO(contents):
    if not contents: return None
    try:
        _, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        return io.StringIO(decoded.decode('utf-8'))
    except Exception as e:
        print(f"Error processing uploaded file contents: {e}")
        return None

# Template for error messages on the plot
error_dict_template = {
    "data": [],
    "layout": {
        "title": "Error",
        "xaxis": {"visible": False},
        "yaxis": {"visible": False},
        "annotations": [{
            "text": "Could not generate plot.", "xref": "paper", "yref": "paper",
            "showarrow": False, "font": {"size": 16}
        }]
    }
}

# --- Page Registration ---
# This registers the page with Dash, making it discoverable in the /pages directory
dash.register_page(__name__, path='/interactive', name='Interactive Plot', title='Interactive Plot')

# --- Page Layout ---
layout = html.Div([
    html.H1("Interactive Protein Plot"),
    dcc.Graph(
        id='protein-plot-interactive',
        responsive=True,
        figure=plot_from_strio() # Load initial figure
    ),
    html.Div([
        html.Button("Download Plot Data (CSV)", id="download-csv-interactive", className='material-button'),
        dcc.Upload(
            id='upload-data-interactive',
            children=html.Div(['Upload CSV File'], className='material-button upload-button-link'),
            className='dcc-upload-container',
            multiple=False,
        ),
    ], style={'display': 'flex', 'justifyContent': 'center', 'gap': '20px', 'margin': '20px 0'}),
    dcc.Download(id="download-dataframe-csv-interactive"),
    html.Div(id='error-message-div', style={'textAlign': 'center', 'color': 'red', 'marginTop': '10px'}),
    dcc.Markdown(children=markdown_text('quickstart.md'), mathjax=True),
    html.Img(
        src='/static/excaliprotein.png',
        alt="Excaliprotein Logo",
        style={'width': '40%', 'display': 'block', 'margin': '20px auto', 'padding': '10px 0'}
    ),
])

# --- Callbacks for the Interactive Plot page ---

@callback(
    [Output('protein-plot-interactive', 'figure'),
     Output('error-message-div', 'children')],
    [Input('upload-data-interactive', 'contents')],
    [State('upload-data-interactive', 'filename')],
    prevent_initial_call=True # Prevents this from running on page load
)
def update_graph_interactive(contents, filename):
    if contents is None:
        return no_update, no_update

    strio = contents_to_stringIO(contents)
    if isinstance(strio, io.StringIO):
        try:
            fig_data = plot_from_strio(strio)
            return fig_data, ""
        except Exception as e:
            error_msg = f"Error generating plot from uploaded file '{filename}': {e}"
            rdict = dict(error_dict_template)
            rdict['layout']['annotations'][0]['text'] = f"Error: {e}"
            rdict['layout']['title'] = f"Failed to plot {filename}"
            return rdict, error_msg
    else:
        error_msg = f"Error processing uploaded file '{filename}'."
        rdict = dict(error_dict_template)
        rdict['layout']['annotations'][0]['text'] = "Invalid file content."
        rdict['layout']['title'] = "File Processing Error"
        return rdict, error_msg

@callback(
    Output("download-dataframe-csv-interactive", "data"),
    [Input("download-csv-interactive", "n_clicks")],
    prevent_initial_call=True,
)
def download_csv_interactive(n_clicks):
    if proteinplot_instance and hasattr(proteinplot_instance, 'df') and proteinplot_instance.df is not None:
        try:
            return dcc.send_data_frame(proteinplot_instance.df.to_csv, "proteinplot_data.csv", index=False)
        except Exception as e:
            print(f"Error preparing CSV for download: {e}")
            return None
    print("No data frame available for download or proteinplot_instance not ready.")
    return None
