import streamlit as st
import pandas as pd
from snowflake.connector import connect
import plotly.express as px

# Function to connect to Snowflake
def get_snowflake_connection():
    return connect(
        user='<username>',          # Replace with your Snowflake username
        password='<password>',  # Replace with your Snowflake password
        account='<account_url>',    # Replace with your Snowflake account
        warehouse='PROJECT_WH',# Replace with your Snowflake warehouse
        database='ANALYTICS',  # Replace with your Snowflake database
        schema='REPORT_SCHEMA' # Replace with your Snowflake schema
    )

# Streamlit app
st.title("Regional Sales Analysis")

# Fetch data from Snowflake
conn = get_snowflake_connection()
query = "SELECT * FROM regional_sales_analysis"  # Your SQL query to fetch the data
df = pd.read_sql(query, conn)

# Display the DataFrame in Streamlit
st.dataframe(df)

# Visualizing the revenue of the regions
if 'REGION_NAME' in df.columns and 'TOTAL_REVENUE' in df.columns:  # Ensure the relevant columns exist
    st.bar_chart(df.set_index('REGION_NAME')['TOTAL_REVENUE'])  # Bar chart visualization

    # Create a map visualization
    fig = px.choropleth(
        df,
        locations='REGION_NAME',  # This column should represent regions
        locationmode='country names',  # Change if needed
        color='TOTAL_REVENUE',  # Column with revenue
        hover_name='REGION_NAME',  # Hover data
        title='Total Revenue by Region',
        color_continuous_scale=px.colors.sequential.Plasma
    )

    st.plotly_chart(fig)  # Display the plotly map in Streamlit
else:
    st.warning("TOTAL_REVENUE or REGION_NAME column not found in the data.")

# Close the connection
conn.close()
