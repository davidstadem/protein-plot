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


def main():
    df = read_df()
    df = clean_df(df)
    fig=make_plot(df)
    fig.show()

if __name__ == '__main__':
    main()