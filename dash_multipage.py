from dash import dcc, html, Dash
import dash
import os

# --- App Initialization ---

# Add external stylesheets and enable the 'pages' feature
external_stylesheets = ['/assets/style.css']
app = Dash(__name__, use_pages=True, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)
server = app.server # Expose server for deployments

# --- Shared Helper Functions ---

def markdown_text(filepath):
    try:
        with open(filepath, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading markdown file {filepath}: {e}")
        return f"Error reading {filepath}."

# --- Static Page Layouts ---

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

# Register Home and About pages manually
# This is an alternative to putting them in the /pages folder
dash.register_page('home', path='/', layout=layout_home, name='Home', title='Home')
dash.register_page('about', path='/about', layout=layout_about, name='About', title='About')


# --- Main App Layout ---
# This layout is common to all pages
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    
    # Navigation bar - dynamically created from registered pages
    html.Nav([
        html.Ul([
            html.Li(dcc.Link(page['name'], href=page['relative_path']))
            for page in dash.page_registry.values()
        ], className='navbar-list')
    ], className='navbar'),

    # dash.page_container is where the content of each page will be rendered
    dash.page_container
])

# --- Main Execution ---
if __name__ == '__main__':
    app.run_server(debug=True)
