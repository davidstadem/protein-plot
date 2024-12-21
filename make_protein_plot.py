import pandas as pd

PRICESPATH = 'prices.csv'

def read_df():
    df=pd.read_csv(PRICESPATH)
    return df


def cleandollars(s):
    return float(s.strip().strip('$'))


def price_per_g_protein(ser):
    priceperserving = ser['Price']/ser['Servings per container']
    pricepergprotein = priceperserving/ser['Protein g']
    return pricepergprotein


CALS_PER_G = {
    'Fat g':9, 
    'Carb g':4,
    'Protein g':4,
}
 

def proteindensity(ser, use_given_cals=True):
    
    cals = ser['Calories per serving']
    tots = ser.loc[CALS_PER_G.keys()]*list(CALS_PER_G.values())
    if not use_given_cals:
        cals=tots.sum()
    pcp = tots['Protein g']/cals
    return pcp

def clean_df(df):
    df['Price'] = df['Price'].apply(cleandollars)
    df['DPG'] = df.apply(price_per_g_protein, axis=1)*100
    df['PCP'] = df.apply(proteindensity, axis=1)
    return df

def make_plot(df):
    import plotly.express as px

    fig=px.scatter(df,
        x='PCP',
        y='DPG',
        text='Name',
        
    )
    fig.update_traces(
        mode='text'
    )

    fig.update_layout(
        yaxis_range=(0,11.5),
        xaxis_range=(0,1),
        yaxis_tickprefix = '$',
        yaxis_tickformat='.2f',
        xaxis_tickformat='.0%',
    )
    return fig

import plotly.graph_objects as go
import numpy as np

def add_contour(fig, func, x_range, y_range, contour_kwargs=None):
    """
    Adds a contour plot to an existing Plotly figure.

    Args:
        fig: The existing Plotly figure (go.Figure object).
        func: The function to evaluate for the contour plot. Must accept two numpy arrays as input.
        x_range: A tuple (min, max) defining the x-axis range.
        y_range: A tuple (min, max) defining the y-axis range.
        contour_kwargs: Optional dictionary of keyword arguments passed to go.Contour.

    Returns:
        The updated Plotly figure.
        Raises ValueError if x or y range are invalid.
    """

    if x_range[0] >= x_range[1]:
        raise ValueError("Invalid x_range: min must be less than max")
    if y_range[0] >= y_range[1]:
        raise ValueError("Invalid y_range: min must be less than max")

    x = np.linspace(x_range[0], x_range[1], 100)  # Adjust resolution as needed
    y = np.linspace(y_range[0], y_range[1], 100)
    X, Y = np.meshgrid(x, y)
    Z = func(X, Y)

    default_contour_kwargs = dict(
        contours_coloring = 'heatmap',
        line_width = 0,
        line_color = None,
        ncontours = 20,
        opacity = 0.7,
        colorscale='Electric',
    )
    if contour_kwargs is not None:
        default_contour_kwargs.update(contour_kwargs)

    contour = go.Contour(
        x=x,
        y=y,
        z=Z,
        **default_contour_kwargs
    )

    fig.add_trace(contour)
    fig.update_layout(uirevision="constant")
    new_data = list(fig.data)  # Convert fig.data to a list (mutable)
    contour_trace = new_data.pop()  # Remove the last trace (the contour) using pop on the list
    new_data.insert(0, contour_trace)  # Insert it at the beginning
    fig.data = tuple(new_data)  # Convert the modified list back to a tuple
    
    return fig


# Example usage:
def my_function(x, y):
    return x-.2*y


def main():
    df = read_df()
    df = clean_df(df)
    fig=make_plot(df)
    fig=add_contour(fig,my_function,x_range=(0,1),y_range=(0,11))
    fig.show()

if __name__ == '__main__':
    main()