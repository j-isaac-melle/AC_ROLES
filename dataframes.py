     
#dont run anything past while troubleshooting:
import streamlit
import snowflake.connector
import pandas

streamlit.title('Air Canada Webpage')

streamlit.header('Users & Roles')
streamlit.text('USER: An identiy recognized by Snowflake, associated to Person or Program (Azure x Air Canada).\n')
streamlit.text('ROLE: An entity to which privileges can be granted.')
streamlit.text('\tRoles are assigned to users.')
streamlit.text('\tRoles may also be assigned to other roles, creating a role hierarchy.')
streamlit.header('Check out our users:')

#streamlit.multiselect(

#streamlit.dataframe()


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake2"])

my_cur = my_cnx.cursor()

my_cur.execute("SELECT * FROM PC_RIVERY_DB.PUBLIC.USERS")
myresult = my_cur.fetchall()


streamlit.dataframe(myresult)


#streamlit.header('Check out our Roles:')
#my_cur.execute("SELECT * FROM PC_RIVERY_DB.PUBLIC.OUR_ROLES")
#myresult = my_cur.fetchall()
#streamlit.multiselect("Pick a user: ", list(my_cur.index))
#streamlit.dataframe(myresult)
