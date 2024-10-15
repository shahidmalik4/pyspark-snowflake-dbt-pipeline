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

# Set page layout to wide
st.set_page_config(layout="wide")

# Cache Snowflake query results to avoid redundant fetches
@st.cache_data(ttl=3600)  # Cache the data for 1 hour (TTL in seconds)
def fetch_data_from_snowflake(query):
    conn = get_snowflake_connection()  # Establish the connection
    try:
        # Execute the query and fetch the results into a pandas DataFrame
        df = pd.read_sql(query, conn)
    finally:
        conn.close()  # Ensure the connection is closed after fetching the data
    return df

# Centered Title using markdown with HTML and full-width CSS
st.markdown("""
    <style>
        .centered-title {
            text-align: center;
            width: 100%;
        }
        .full-width-tabs > div[role="tablist"] {
            justify-content: center;
        }
    </style>
    <h1 class="centered-title">Sales Analysis Dashboard</h1>
""", unsafe_allow_html=True)

# Wrap the tabs in a container with full-width
tabs_container = st.container()

with tabs_container:
    st.markdown('<div class="full-width-tabs">', unsafe_allow_html=True)
    # Create tabs
    tab1, tab2, tab3 = st.tabs(["Customer Analysis", "Products Analysis", "Territorial Analysis"])
    st.markdown('</div>', unsafe_allow_html=True)

# Customer Analysis
with tab1:
    st.header("Customer Analysis")
    customer_query = "SELECT * FROM ANALYTICS.REPORT_SCHEMA.TOP_PRODUCTS_BY_REVENUE LIMIT 1000"  # Your SQL query for customer data
    customer_df = fetch_data_from_snowflake(customer_query)  # Use cached data fetching
    
    # Display the DataFrame
    st.dataframe(customer_df)

    # Visualize customer data
    if 'PRODUCT_NAME' in customer_df.columns and 'TOTAL_REVENUE' in customer_df.columns:
        # Create a horizontal bar chart using Plotly
        fig = px.bar(customer_df, 
                     x='TOTAL_REVENUE', 
                     y='PRODUCT_NAME', 
                     orientation='h',  # Set orientation to horizontal
                     title='Total Revenue by Product',
                     labels={'TOTAL_REVENUE': 'Total Revenue', 'PRODUCT_NAME': 'Product Name'})
        
        # Update layout to change the cursor to arrow on hover
        fig.update_layout(hovermode='closest', 
                          hoverlabel=dict(bgcolor="white"),
                          margin=dict(l=20, r=20, t=50, b=20))
        
        # Add CSS to change the cursor to an arrow
        st.markdown(
            """
            <style>
            .plotly .hovertext {
                cursor: default !important; /* Change cursor to default arrow */
            }
            </style>
            """, unsafe_allow_html=True
        )

        # Show the Plotly figure in Streamlit
        st.plotly_chart(fig)
    else:
        st.warning("PRODUCT_NAME or TOTAL_REVENUE column not found in the data.")


# Products Analysis
with tab2:
    st.header("Products Analysis")
    product_query = "SELECT * FROM ANALYTICS.REPORT_SCHEMA.TOP_N_PRODUCTS_BY_SALES"  # Your SQL query for product data
    product_df = fetch_data_from_snowflake(product_query)  # Use cached data fetching

    # Display the DataFrame
    st.dataframe(product_df)

    # Visualize product data
    if 'PRODUCT_NAME' in product_df.columns and 'TOTAL_SALES' in product_df.columns:
        st.bar_chart(product_df.set_index('PRODUCT_NAME')['TOTAL_SALES'])  # Bar chart for total sales by product
    else:
        st.warning("PRODUCT_NAME or TOTAL_SALES column not found in the data.")

# Territorial Analysis
with tab3:
    st.header("Territorial Analysis")
    territory_query = "SELECT * FROM ANALYTICS.REPORT_SCHEMA.REGIONAL_SALES_ANALYSIS"  # Your SQL query for regional data
    territory_df = fetch_data_from_snowflake(territory_query)  # Use cached data fetching

    # Display the DataFrame
    st.dataframe(territory_df)

    # Visualizing the revenue by regions
    if 'REGION_NAME' in territory_df.columns and 'TOTAL_REVENUE' in territory_df.columns:
        st.bar_chart(territory_df.set_index('REGION_NAME')['TOTAL_REVENUE'])  # Bar chart for revenue by region

        # Create a map visualization
        fig = px.choropleth(
            territory_df,
            locations='REGION_NAME',  # This column should represent regions
            locationmode='country names',  # Adjust as necessary
            color='TOTAL_REVENUE',  # Column with revenue
            hover_name='REGION_NAME',  # Hover data
            title='Total Revenue by Region',
            color_continuous_scale=px.colors.sequential.Plasma
        )
        st.plotly_chart(fig)  # Display the map
    else:
        st.warning("REGION_NAME or TOTAL_REVENUE column not found in the data.")
