import dash
from dash import dcc, html, Input, Output, State, callback, no_update, dash_table
import io
import base64
import os
import pandas as pd

# --- Page-Specific Dependencies & Helpers ---

# Attempt to import protein_plot, handle if not found for basic structure.
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
            self.df = pd.DataFrame(columns=['Name', 'Price', 'Servings per container', 'Calories per serving', 'Fat g', 'Carb g', 'Protein g'])
        def read_df(self, strio): 
            self.df = pd.read_csv(strio)
        def clean_df(self): pass
        def make_plot(self): pass
        def add_contour(self, y_range):
            return {"data": [], "layout": {"title": "Protein Plot (Data Missing)"}}
        def append_newdata(self, dfnew):
             self.df = pd.concat([self.df, dfnew], ignore_index=True)

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

# Helper function to generate plot from data, now accepts user data
def generate_plot(base_strio=None, user_data=None):
    if proteinplot_instance is None:
        return {"data": [], "layout": {"title": "Plotting module not loaded."}}
    
    # Determine the base data to load
    strio_path = base_strio if base_strio is not None else PRICESPATH
    if strio_path is None:
        from io import StringIO
        dummy_csv = "Name,Price,Servings per container,Calories per serving,Fat g,Carb g,Protein g\nProteinA,10,1,100,5,10,15\nProteinB,20,1,200,10,20,30"
        strio_path = StringIO(dummy_csv)
        print("Using dummy CSV data for initial plot as PRICESPATH is not available.")

    # Load base data
    proteinplot_instance.read_df(strio_path)
    
    # Append user-added data if it exists
    if user_data:
        df_user = pd.DataFrame(user_data)
        proteinplot_instance.append_newdata(df_user)

    # Generate the plot
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
    "data": [], "layout": { "title": "Error", "xaxis": {"visible": False}, "yaxis": {"visible": False},
        "annotations": [{"text": "Could not generate plot.", "xref": "paper", "yref": "paper", "showarrow": False, "font": {"size": 16}}]
    }
}

# --- Page Registration ---
dash.register_page(__name__, path='/interactive', name='Interactive Plot', title='Interactive Plot')

# --- Page Layout ---
TABLE_COLUMNS = ['Name', 'Price', 'Servings per container', 'Calories per serving', 'Fat g', 'Carb g', 'Protein g']
EMPTY_TABLE_DATA = [{col: '' for col in TABLE_COLUMNS} for i in range(3)]

layout = html.Div(className='page-container', children=[
    # This component stores user-added data in their browser session
    dcc.Store(id='user-data-store', storage_type='session'),

    html.H1("Interactive Protein Plot"),

    # Section 1: The Plot
    html.Div(id='plot-container', className='plot-container', children=[
        dcc.Graph(
            id='protein-plot-interactive', 
            responsive=True,
            style={'height': '70vh', 'width': '100%'} # This line fixes the overlap
        )
    ]),
    
    # Section 2: Controls (Buttons)
    html.Div(className='controls-container', children=[
        html.Div(className='button-group', children=[
            html.Button("Download Plot Data (CSV)", id="download-csv-interactive", className='material-button'),
            dcc.Upload(
                id='upload-data-interactive',
                children=html.Div(['Upload New CSV File (Resets Plot)'], className='material-button upload-button-link'),
                className='dcc-upload-container', 
                multiple=False,
            ),
        ]),
    ]),
    dcc.Download(id="download-dataframe-csv-interactive"),
    html.Div(id='error-message-div', style={'textAlign': 'center', 'color': 'red'}),
    
    # Section 3: Data Table for adding food
    html.Div(className='data-table-container', children=[
        html.Hr(style={'width': '100%'}),
        html.H3("Add Your Own Foods"),
        html.P("Enter food details below. Click 'Add Foods to Plot' to update the graph. Data persists on refresh."),
        dash_table.DataTable(
            id='add-food-table',
            columns=[{"name": i, "id": i} for i in TABLE_COLUMNS],
            data=EMPTY_TABLE_DATA,
            editable=True,
            row_deletable=True,
            style_cell={'textAlign': 'left', 'padding': '5px'},
            style_header={'backgroundColor': 'rgb(230, 230, 230)', 'fontWeight': 'bold'},
            style_data_conditional=[{'if': {'row_index': 'odd'}, 'backgroundColor': 'rgb(248, 248, 248)'}],
            style_table={'width': '100%', 'minWidth': '100%'}
        ),
        html.Button('Add Foods to Plot', id='add-foods-button', n_clicks=0, className='material-button'),
        html.Hr(style={'width': '100%'}),
    ]),

    dcc.Markdown(children=markdown_text('quickstart.md'), mathjax=True),
    html.Img(
        src='/static/excaliprotein.png', alt="Excaliprotein Logo",
        style={'width': '40%', 'display': 'block', 'margin': '20px auto', 'padding': '10px 0'}
    ),
])

# --- Main Callback to control the page ---
@callback(
    Output('plot-container', 'children'),
    Output('user-data-store', 'data'),
    Output('add-food-table', 'data'),
    Output('error-message-div', 'children'),
    Input('upload-data-interactive', 'contents'),
    Input('add-foods-button', 'n_clicks'),
    State('upload-data-interactive', 'filename'),
    State('add-food-table', 'data'),
    State('user-data-store', 'data'),
    # This dummy input ensures the callback runs on page load to load stored data
    Input('plot-container', 'id') 
)
def update_plot_and_store(contents, n_clicks, filename, table_rows, stored_data, _):
    # Determine what triggered the callback
    ctx = dash.callback_context
    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0] if ctx.triggered else 'initial_load'

    error_msg = ""
    user_data = stored_data or []
    new_table_data = no_update
    fig = no_update

    if triggered_id == 'upload-data-interactive' and contents:
        # A new file upload RESETS everything
        user_data = [] # Clear stored data
        new_table_data = EMPTY_TABLE_DATA # Reset table
        strio = contents_to_stringIO(contents)
        if isinstance(strio, io.StringIO):
            fig = generate_plot(base_strio=strio, user_data=None)
        else:
            error_msg = f"Error processing uploaded file '{filename}'."
            fig = generate_plot(user_data=None) # Show default plot on error
    
    elif triggered_id == 'add-foods-button' and table_rows:
        # Add new rows from the table to the stored data
        valid_rows = [row for row in table_rows if row.get('Name')]
        dfnew = pd.DataFrame(valid_rows)
        
        # Clean and validate new data before adding
        for col in ['Price', 'Servings per container', 'Calories per serving', 'Fat g', 'Carb g', 'Protein g']:
            dfnew[col] = pd.to_numeric(dfnew[col], errors='coerce')
        dfnew.dropna(subset=['Price', 'Servings per container', 'Protein g', 'Name'], inplace=True)
        
        if not dfnew.empty:
            # Combine with existing stored data
            user_data.extend(dfnew.to_dict('records'))
            new_table_data = EMPTY_TABLE_DATA # Clear the input table
        
        fig = generate_plot(user_data=user_data)

    else: # Initial page load
        fig = generate_plot(user_data=user_data)

    # Always return a full dcc.Graph component to prevent layout breaks
    graph_component = dcc.Graph(
        id='protein-plot-interactive', 
        responsive=True, 
        figure=fig,
        style={'height': '70vh', 'width': '100%'}
    )
    return graph_component, user_data, new_table_data, error_msg

# --- Download Callback ---
@callback(
    Output("download-dataframe-csv-interactive", "data"),
    Input("download-csv-interactive", "n_clicks"),
    prevent_initial_call=True,
)
def download_csv_interactive(n_clicks):
    # The proteinplot_instance is now a global-like object updated by the main callback
    if proteinplot_instance and hasattr(proteinplot_instance, 'df') and proteinplot_instance.df is not None:
        try:
            return dcc.send_data_frame(proteinplot_instance.df.to_csv, "proteinplot_data.csv", index=False)
        except Exception as e:
            print(f"Error preparing CSV for download: {e}")
            return None
    return None
