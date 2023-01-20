import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('Air Canada Roles & Users')

# Example 1

st.write('Data Table 1:')

# Example 2

st.write(1234)

# Example 3

df = pd.DataFrame({
      'User': ['jonathan.melle@aircanada.ca','jonathan.melle@aircanada.ca'],
      'Roles': ['usr_jonathan_melle', 'accountadmin']
     })
st.write(df)

# Example 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
