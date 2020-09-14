import streamlit as st
x = st.slider('x')
st.write(x, 'squared is', x * x)

url = st.text_input('Enter URL')
st.write('The entered URL is', url)

import pandas as pd
import numpy as np
df = pd.read_csv("football_data.csv")

# To show dataframe with a checkbox
if st.checkbox('Show DataFrame'):
    st.write(df.head())

# 4. SelectBox like a LOV
option = st.selectbox("Which Club do you like best?",
                     df['Club'].unique())
'You selected: ', option

# 5. Multiselect from a dropdown
options = st.multiselect('What are your favorite clubs?',
                        df['Club'].unique())
st.write('You selected: ', options)  


