import plotly.express as px
import numpy as np
import pandas as pd

def interactive_plot(df):
    fig=px.line()
    for i in df.columns[1:]:
        fig.add_scatter(x=df['Date'],y=df[i],name=i)
    fig.update_layout(width=450,margin = dict(l=20,r=20,t=50,b=20),legend=dict(orientation='h',yanchor='bottom',
    y=1.02,xanchor='right',x=1,))
    return fig



def normalize(df):
    # Check each column to ensure it is numeric before normalizing
    for i in df.columns:
        if pd.api.types.is_numeric_dtype(df[i]):
            df[i] = df[i] / df[i].iloc[0]
    return df


import pandas as pd

import pandas as pd

def daily_returns(df):
    # Ensure the DataFrame only contains numeric columns
    numeric_df = df.select_dtypes(include=['number'])
    
    print("DataFrame before calculating daily returns:")
    print(numeric_df.head())
    
    # Calculate daily returns using pct_change
    df_daily_return = numeric_df.pct_change() * 100
    
    # Fill NaN values (typically the first row) with 0
    df_daily_return.fillna(0, inplace=True)
    
    print("DataFrame after calculating daily returns:")
    print(df_daily_return.head())
    
    return df_daily_return

# Example usage in your script
import streamlit as st
import CAPM_functions

def calculate_beta(stocks_daily_return,stock):
    rm=stocks_daily_return['sp500'].mean()*252

    b,a=np.polyfit(stocks_daily_return['sp500'],stocks_daily_return[stock],1)
    return b,a