import pandas as pd

PRICESPATH = 'prices.csv'

df=pd.read_csv(PRICESPATH)

ser=df.loc[0]

s=ser['Price']
def cleandollars(s):
    return float(s.strip().strip('$'))

df['Price'] = df['Price'].apply(cleandollars)

def price_per_g_protein(ser):
    priceperserving = ser['Price']/ser['Servings per container']/ser['Number']
    pricepergprotein = priceperserving/ser['Protein g']
    return pricepergprotein

df['DPG'] = df.apply(price_per_g_protein, axis=1)*100

calsperg = {
    'Fat g':9, 
    'Carb g':4,
    'Protein g':4,
}
 

def proteindensity(ser, use_given_cals=True):
    
    cals = ser['Calories per serving']
    tots = ser.loc[calsperg.keys()]*list(calsperg.values())
    if not use_given_cals:
        cals=tots.sum()
    pcp = tots['Protein g']/cals
    return pcp

df['PCP'] = df.apply(proteindensity, axis=1)

import plotly.express as px

px.scatter(df,
    x='PCP',
    y='DPG',
    text='Name',
).show()