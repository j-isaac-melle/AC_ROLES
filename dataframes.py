import numpy as np
import altair as alt
import pandas as pd
import streamlit as st




st.header('Air Canada Roles & Users')

# Example 1

st.write('Data Table 1:')

# Example 2

st.write('1 user: 2 roles')

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


import streamlit as st
from datetime import time, datetime

st.header('st.slider')

# Example 1

st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# Example 2

st.subheader('Range slider')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

# Example 3
#Range of time
st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

# Example 4
#Date slider
st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

#random numbers line chart
st.header('Random number --> a,b,c')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

#Favorite color selector:

st.header('Role Picker')

option = st.selectbox(
     'Pick a role',
     ('AccountAdmin', 'Sysadmin', 'usr_jonathan_melle'))

st.write('Roles ', option)
