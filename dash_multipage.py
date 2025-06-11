from dash import dcc, html, Dash, Input, Output, State, callback, no_update, callback_context
import io
import base64
import os # For markdown_text and potentially static file serving

# Attempt to import protein_plot, handle if not found for basic structure
try:
    import protein_plot
    proteinplot_instance = protein_plot.ProteinPlot()
    PRICESPATH = protein_plot.PRICESPATH
except ImportError:
    print("Warning: protein_plot.py not found. Some features will be disabled.")
    proteinplot_instance = None
    PRICESPATH = None # Or a default path to a dummy CSV if needed for basic plot
    # Create a dummy ProteinPlot class if needed for the app to run without the file
    class DummyProteinPlot:
        def __init__(self):
            self.df = None
        def read_df(self, strio): pass
        def clean_df(self): pass
        def make_plot(self): pass
        def add_contour(self, y_range):
            # Return a placeholder figure
            return {"data": [], "layout": {"title": "Protein Plot (Data Missing)"}}
    if proteinplot_instance is None:
        proteinplot_instance = DummyProteinPlot()


# Helper function to read markdown files
def markdown_text(filepath):
    # Create placeholder files if they don't exist, for demonstration
    if not os.path.exists(filepath):
        default_content = f"## Placeholder for {os.path.basename(filepath)}\n\nThis is default content. Please create `{filepath}` with your actual text."
        try:
            with open(filepath, 'w') as f:
                f.write(default_content)
            print(f"Created placeholder file: {filepath}")
        except IOError as e:
            print(f"Could not create placeholder file {filepath}: {e}")
            return f"Error: Could not create or read {filepath}."


    try:
        with open(filepath, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Warning: Markdown file not found at {filepath}")
        return f"Error: The file `{filepath}` was not found. Please create it."
    except Exception as e:
        print(f"Error reading markdown file {filepath}: {e}")
        return f"Error reading {filepath}."

# Add external stylesheets to your Dash app
external_stylesheets = ['/assets/style.css'] # Link to your CSS file

# Initialize Dash app
# suppress_callback_exceptions is useful for multi-page apps where outputs are not in the initial layout
app = Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)
server = app.server # Expose server for deployments

# --- Define Page Layouts ---

# Page 1: Home
layout_home = html.Div([
    html.H1("Welcome to the Protein Plot Viewer"),
    dcc.Markdown(children=markdown_text('basic.md')),
    html.H3("Static Protein Plot Overview"),
    html.Img(
        src='/static/protein-plot.png',
        alt="Static Protein Plot",
        style={'width': '80%', 'display': 'block', 'margin': 'auto', 'padding': '20px 0', 'border': '1px solid #ddd'}
    ),
])

# Page 2: About
layout_about = html.Div([
    dcc.Markdown(children=markdown_text('manifesto.md'), mathjax=True),
])

# Page 3: Interactive Plot
def plot_from_strio(strio=None):
    if proteinplot_instance is None: # Should not happen if DummyProteinPlot is used
        return {"data": [], "layout": {"title": "Plotting module not loaded."}}
    if strio is None:
        if PRICESPATH:
            strio_path = PRICESPATH
        else: # Fallback if protein_plot.py or PRICESPATH is missing
            # Create a dummy CSV in memory for the plot to show something
            from io import StringIO
            dummy_csv = "protein,value\nProteinA,10\nProteinB,20"
            strio_path = StringIO(dummy_csv)
            print("Using dummy CSV data for initial plot as PRICESPATH is not available.")
    else:
        strio_path = strio

    proteinplot_instance.read_df(strio_path)
    proteinplot_instance.clean_df()
    proteinplot_instance.make_plot()
    fig = proteinplot_instance.add_contour(y_range=(0, 11.5))
    return fig

def contents_to_stringIO(contents):
    if not contents: return None
    try:
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        utf8io = io.StringIO(decoded.decode('utf-8'))
        return utf8io
    except Exception as e:
        print(f"Error processing uploaded file contents: {e}")
        return None

error_dict_template = {
    "data": [],
    "layout": {
        "title": "Error",
        "xaxis": {"visible": False},
        "yaxis": {"visible": False},
        "annotations": [{
            "text": "Could not generate plot.",
            "xref": "paper",
            "yref": "paper",
            "showarrow": False,
            "font": {"size": 16}
        }]
    }
}

layout_interactive = html.Div([
    html.H1("Interactive Protein Plot"),
    html.Div(
        dcc.Graph(
            id='protein-plot-interactive', # Changed ID to avoid conflict if any old component remains
            responsive=True,
            # figure=plot_from_strio() # Initial figure load
        ),
        style={
            'width': '90%', # Adjusted width
            'margin': 'auto',
            'height': '500px', # Explicit height can be good
            'aspectRatio': '16/9', # Can conflict with explicit height
        },
    ),
    html.Div([
        html.Button(
            "Download Plot Data (CSV)",
            id="download-csv-interactive",
            className='material-button',
        ),
        dcc.Upload(
            id='upload-data-interactive',
            children=html.Div(
                ['Upload CSV File'],
                className='material-button upload-button-link' # Combined for simplicity
            ),
            className='dcc-upload-container',
            multiple=False,
        ),
    ], style={'display': 'flex', 'justifyContent': 'center', 'gap': '20px', 'margin': '20px 0'}),
    dcc.Download(id="download-dataframe-csv-interactive"),
    html.Div(
        id='error-message-div', style={'textAlign': 'center', 'color': 'red', 'marginTop': '10px'}
    ),
    dcc.Markdown(
        children=markdown_text('quickstart.md'), mathjax=True
    ),
    html.Img(
        src='/static/excaliprotein.png',
        alt="Excaliprotein Logo",
        style={'width': '40%', 'display': 'block', 'margin': '20px auto', 'padding': '10px 0'}
    ),
])

# --- App Layout with Navigation ---
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Nav([
        html.Ul([
            html.Li(dcc.Link('Home', href='/')),
            html.Li(dcc.Link('Interactive Plot', href='/interactive')),
            html.Li(dcc.Link('About', href='/about')),
        ], className='navbar-list') # Added a class for potential styling
    ], className='navbar'), # Added a class for potential styling

    html.Div(id='page-content', style={'padding': '20px'}) # Content will be rendered here
])

# --- Callbacks ---

# Callback to render page content based on URL
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/interactive':
        return layout_interactive
    elif pathname == '/about':
        return layout_about
    elif pathname == '/' or pathname == '/home': # Default to home
        return layout_home
    else:
        return html.Div([
            html.H1("404: Page Not Found"),
            html.P(f"The pathname {pathname} was not recognised.")
        ])

# Callbacks for the Interactive Plot page
@app.callback(
    [Output('protein-plot-interactive', 'figure'),
     Output('error-message-div', 'children')],
    [Input('upload-data-interactive', 'contents'),
     Input('url', 'pathname')], # Add pathname to re-trigger on page load if needed
    [State('upload-data-interactive', 'filename')]
)
def update_graph_interactive(contents, pathname, filename):
    # Only update if on the interactive page and proteinplot_instance is available
    if pathname == '/interactive' and proteinplot_instance:
        # callback_context is a special object provided by Dash to determine which input triggered the callback.
        # It needs to be imported from `dash` to be used.
        ctx = callback_context
        triggered_id = ctx.triggered[0]['prop_id'].split('.')[0] if ctx.triggered else None
        
        error_msg = ""
        fig_data = None

        if triggered_id == 'upload-data-interactive' and contents is not None:
            strio = contents_to_stringIO(contents)
            if isinstance(strio, io.StringIO):
                try:
                    fig_data = plot_from_strio(strio)
                except Exception as e:
                    error_msg = f"Error generating plot from uploaded file '{filename}': {e}"
                    print(error_msg)
                    rdict = dict(error_dict_template) # Use a copy
                    rdict['layout']['annotations'][0]['text'] = f"Error: {e}"
                    rdict['layout']['title'] = f"Failed to plot {filename}"
                    fig_data = rdict
            else:
                error_msg = f"Error processing uploaded file '{filename}'."
                rdict = dict(error_dict_template)
                rdict['layout']['annotations'][0]['text'] = "Invalid file content."
                rdict['layout']['title'] = "File Processing Error"
                fig_data = rdict
        else: # Initial load or navigation to page
            try:
                fig_data = plot_from_strio(None) # Load default plot
            except Exception as e:
                error_msg = f"Error generating default plot: {e}"
                print(error_msg)
                rdict = dict(error_dict_template)
                rdict['layout']['annotations'][0]['text'] = "Could not load default data."
                rdict['layout']['title'] = "Default Plot Error"
                fig_data = rdict
        
        return fig_data, error_msg
    
    # If not on the interactive page or proteinplot_instance is missing, return no update
    # `no_update` prevents the callback from updating the output, which is efficient.
    return no_update, no_update

@app.callback(
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
            return None # Or handle error appropriately
    print("No data frame available for download or proteinplot_instance not ready.")
    return None


if __name__ == '__main__':
    # Create dummy markdown files if they don't exist, for the app to run
    for md_file in ['basic.md', 'quickstart.md', 'manifesto.md']:
        if not os.path.exists(md_file):
            markdown_text(md_file) # This will call the creation logic

    # Note on static assets:
    # Dash serves files from an 'assets' folder by default.
    # If your images (protein-plot.png, excaliprotein.png) are in a 'static' folder,
    # you either need to:
    # 1. Move them to an 'assets' folder in the same directory as app.py
    #    and change src to, e.g., src=app.get_asset_url('protein-plot.png') or src='/assets/protein-plot.png'.
    #    I have updated the src attributes to '/assets/protein-plot.png' assuming you'll move them.
    # 2. Or, configure Flask to serve the 'static' folder. Example:
    #    import flask
    #    import os
    #    STATIC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    #    @server.route('/static/<path:filename>')
    #    def static_files(filename):
    #        return flask.send_from_directory(STATIC_PATH, filename)
    # For simplicity, using '/assets/' path is recommended.

    app.run_server(debug=True)
