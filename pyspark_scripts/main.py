import pyspark
from pyspark.sql import SparkSession
from transformations import (
                                transform_supplier, transform_nation, transform_region, transform_part,
                                transform_partsupp, transform_lineitem, transform_orders, transform_customer
                            )


# Initialize the Spark session with Snowflake configurations
spark = SparkSession.builder \
    .appName("PySpark Snowflake DBT ETL") \
    .config("spark.jars.packages", "net.snowflake:snowflake-jdbc:3.13.14,net.snowflake:spark-snowflake_2.12:2.10.0-spark_3.0") \
    .config("spark.executor.extraClassPath", "/home/cipher/pyspark_files/snowflake-jdbc-3.13.14.jar:/home/cipher/pyspark_files/spark-snowflake_2.12-2.10.0-spark_3.0.jar") \
    .config("spark.executor.memory", "4g") \
    .getOrCreate()

# Snowflake Source options
sf_source_options = {
    "sfURL": "https://ksb58116.us-east-1.snowflakecomputing.com",
    "sfUser": "cipher",
    "sfPassword": "adminproxy1S$",
    "sfDatabase": "SNOWFLAKE_SAMPLE_DATA",
    "sfSchema": "TPCH_SF1",
    "sfWarehouse": "COMPUTE_WH",
    "sfRole": "ACCOUNTADMIN"
}

# Snowflake Source options
sf_dest_options = {
    "sfURL": "https://ksb58116.us-east-1.snowflakecomputing.com",
    "sfUser": "shahid",
    "sfPassword": "adminproxy1S$",
    "sfDatabase": "ANALYTICS",
    "sfSchema": "TRANSFORM_SCHEMA",
    "sfWarehouse": "PROJECT_WH",
    "sfRole": "SYSADMIN"
}

# Define a dictionary that maps table names to their respective transformation functions
table_transformations = {
    "SUPPLIER": transform_supplier,
    "REGION": transform_region,
    "NATION": transform_nation,
    "CUSTOMER": transform_customer,
    "LINEITEM": transform_lineitem,
    "PART": transform_part,
    "PARTSUPP": transform_partsupp,
    "ORDERS": transform_orders
}

table_limits = {
    "SUPPLIER": 40,
    "NATION": 5,
    "REGION": 5,
    "CUSTOMER": 100,
    "PART": 200,
    "PARTSUPP": 80,
    "LINEITEM": 1000,
    "ORDERS": 400
}

# Loop through each table, extract data, apply the corresponding transformation, and load it back to Snowflake
for table, transformation_func in table_transformations.items():
    print(f"Processing table: {table}")

    # Get the limit for the current table, default to None if not set
    limit = table_limits.get(table)

    # Extract data from Snowflake with an optional limit
    query = f"SELECT * FROM {table}"
    if limit:
        query += f" LIMIT {limit}"

    print(f"Executing query: {query}") 

    df = spark.read \
        .format("snowflake") \
        .options(**sf_source_options) \
        .option("query", query) \
        .load()

    print(f"Number of records loaded: {df.count()}")

    # Apply the corresponding transformation function
    transformed_df = transformation_func(df)

    # Define the target table for the transformed data
    transformed_table = f"{table}_transformed"

    # Load the transformed data back to Snowflake
    transformed_df.write \
        .format("snowflake") \
        .options(**sf_dest_options) \
        .option("dbtable", transformed_table) \
        .mode("append") \
        .save()

    print(f"Finished processing table: {table}")


# Stop the Spark session after the job is done
spark.stop()