import streamlit as st
import pandas as pd
import numpy as np
import plotly_express as px

"""
Caching
In our simple app. We read the pandas dataframe again and again whenever a value changes. 
While it works for the small data we have, it will not work for big data or when we have to do a lot of processing on the data. 
Let us use caching using the st.cache decorator function in streamlit like below.
"""
df = st.cache(pd.read_csv)("football_data.csv")

# For more complex functions
# @st.cache
# def complex_func(a, b):
    # Do something complex

# complex_func(a, b)

# When we mark a function with Streamlit’s cache decorator,
# whenever the function is called streamlit checks the input parameters that you called the function with.
# If this is the first time Streamlit has seen these params, it runs the function and stores the result in a local cache.
# When the function is called the next time, if those params have not changed, Streamlit knows it can skip executing the function altogether.
# It just uses the results from the cache.

# 2. Sidebar
clubs = st.sidebar.multiselect("Show Player for clubs?", df['Club'].unique())
nationalities = st.sidebar.multiselect("Show Player from Nationalities?", df['Nationality'].unique())
new_df = df[(df['Club'].isin(clubs)) & (df['Nationality'].isin(nationalities))]
st.write(new_df)
# Create distplot with custom bin_size
fig = px.scatter(new_df, x="Overall", y="Age", color="Name")
# Plot!
st.plotly_chart(fig)