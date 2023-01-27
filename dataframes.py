import streamlit as st
import numpy as np
import altair as alt
import snowflake.connector
import pandas as pd


# Connect to the Snowflake database
cnx = snowflake.connector.connect(**st.secrets["snowflake3"])
cursor = cnx.cursor()

# Define the SQL query to retrieve the roles and their privileges
#query = """
#SELECT
 #   ROLE_NAME,
#    PRIVILEGE_NAME
#FROM
 #   INFORMATION_SCHEMA.ROLE_PRIVILEGES
#"""

# Execute the query and fetch the results
#cursor.execute(query)
#rows = cursor.fetchall()

st.title("Snowflake Role Governance")

# Create a table to display the results
#st.table(rows)

# Close the cursor and connection
#cursor.close()
#cnx.close()





# MULTISELECT SECTION

number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)

st.header('Role Heirarchy Explorer:')

# Select box 1
st.subheader('Users assigned to Roles:')

option = st.selectbox(
     '',
     ('AccountAdmin', 'Sysadmin'))

st.write('Role: ', option)


#multiselect example:
st.subheader('Roles assigned to users')

options = st.multiselect(
     'Find a User:',
     ['jonathan.melle@aircanada.ca', 'roger.matadeen@aircanada.ca', 'john.smith@aircanada.ca', 'emily.brown@aircanada.ca'])

st.write('You selected:', options)

st.write('Data Table 1:')

# Datatable

st.write('1 user: 2 roles')

# Example 3

df = pd.DataFrame({
      'User': ['jonathan.melle@aircanada.ca','jonathan.melle@aircanada.ca'],
      'Roles': ['usr_jonathan_melle', 'accountadmin']
     })
st.write(df)

#Checkbox
#FILE UPLOADER
st.title('Upload file')

st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('DataFrame')
  st.write(df)
  st.subheader('Descriptive Statistics')
  st.write(df.describe())
else:
  st.info('Upload a CSV file')



st.header('user/role checkbox')

st.write ('Users with/out roles')

users = st.checkbox('Users')
roles = st.checkbox('Roles')

if users:
     st.write("Here are our users:")

if roles: 
     st.write("Here are our roles:")


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

# STREAMLIT LAYOUT: APP

import streamlit as st

st.title('st.form')

# Full example of using the with notation
st.header('1. Example of using `with` notation')
st.subheader('Coffee machine')

with st.form('my_form'):
    st.subheader('**Order your coffee**')

    # Input widgets
    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
    owncup_val = st.checkbox('Bring own cup')

    # Every form must have a submit button
    submitted = st.form_submit_button('Submit')

if submitted:
    st.markdown(f'''
        ☕ You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type_val}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        ''')
else:
    st.write('☝️ Place your order!')


# Short example of using an object notation
st.header('2. Example of object notation')

form = st.form('my_form_2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected value: ', selected_val)


