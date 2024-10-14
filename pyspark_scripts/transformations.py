from pyspark.sql.functions import *
from pyspark.sql.types import *


# SUPPLIER Table Transformation
def transform_supplier(df):
    transformed_df = df \
        .withColumn("SUPP_KEY", when(col("S_SUPPKEY").isNotNull(), col("S_SUPPKEY").cast(IntegerType())).otherwise(-1)) \
        .withColumn("NAME", when(col("S_NAME").isNotNull(), upper(trim(col("S_NAME")))).otherwise("UNKNOWN")) \
        .withColumn("ADDRESS", when(col("S_ADDRESS").isNotNull(), lower(trim(col("S_ADDRESS")))).otherwise("unknown address")) \
        .withColumn("NATION_KEY", when(col("S_NATIONKEY").isNotNull(), col("S_NATIONKEY").cast(IntegerType())).otherwise(-1)) \
        .withColumn("PHONE", when(length(col("S_PHONE")) == 14, col("S_PHONE")).otherwise(None)) \
        .withColumn("ACCTBAL", when(col("S_ACCTBAL").isNotNull(), col("S_ACCTBAL").cast(DoubleType())).otherwise(0.0)) \
        .withColumn("COMMENT", when(col("S_COMMENT").isNotNull(), trim(col("S_COMMENT"))).otherwise("No Comment")) \
        .drop("S_SUPPKEY", "S_NAME", "S_ADDRESS", "S_NATIONKEY", "S_PHONE", "S_ACCTBAL", "S_COMMENT")
    return transformed_df

# REGION Table Transformation
def transform_region(df):
    transformed_df = df \
        .withColumn("REGION_KEY", when(col("R_REGIONKEY").isNotNull(), col("R_REGIONKEY").cast(IntegerType())).otherwise(-1)) \
        .withColumn("NAME", when(col("R_NAME").isNotNull(), upper(trim(col("R_NAME")))).otherwise("UNKNOWN")) \
        .withColumn("COMMENT", when(col("R_COMMENT").isNotNull(), trim(col("R_COMMENT"))).otherwise("No Comment")) \
        .drop("R_REGIONKEY", "R_NAME", "R_COMMENT")
    return transformed_df

# NATION Table Transformation
def transform_nation(df):
    transformed_df = df \
        .withColumn("NATION_KEY", when(col("N_NATIONKEY").isNotNull(), col("N_NATIONKEY").cast(IntegerType())).otherwise(-1)) \
        .withColumn("NAME", when(col("N_NAME").isNotNull(), upper(trim(col("N_NAME")))).otherwise("UNKNOWN")) \
        .withColumn("REGION_KEY", when(col("N_REGIONKEY").isNotNull(), col("N_REGIONKEY").cast(IntegerType())).otherwise(-1)) \
        .withColumn("COMMENT", when(col("N_COMMENT").isNotNull(), trim(col("N_COMMENT"))).otherwise("No Comment")) \
        .drop("N_NATIONKEY", "N_NAME", "N_REGIONKEY", "N_COMMENT")
    return transformed_df

# CUSTOMER Table Transformation
def transform_customer(df):
    transformed_df = df \
        .withColumn("CUST_KEY", trim(col("C_CUSTKEY"))) \
        .withColumn("NAME", lower(trim(col("C_NAME")))) \
        .withColumn("ADDRESS", lower(trim(col("C_ADDRESS")))) \
        .withColumn("PHONE", when(length(col("C_PHONE")) == 14, col("C_PHONE")).otherwise(None)) \
        .withColumn("MKTSEGMENT", lower(trim(col("C_MKTSEGMENT")))) \
        .withColumn("NATION_KEY", col("C_NATIONKEY").cast(IntegerType())) \
        .withColumn("ACCTBAL", when(col("C_ACCTBAL") > 0, col("C_ACCTBAL")).otherwise(0)) \
        .withColumn("FULL_INFO", concat_ws(", ", col("C_NAME"), col("C_ADDRESS"), col("C_PHONE"))) \
        .withColumn("COMMENT", when(col("C_COMMENT").isNotNull(), trim(col("C_COMMENT"))).otherwise("No Comment")) \
        .drop("C_CUSTKEY", "C_NAME", "C_ADDRESS", "C_PHONE", "C_MKTSEGMENT", "C_NATIONKEY", "C_ACCTBAL", "C_COMMENT")
    return transformed_df

# ORDERS Table Transformation
def transform_orders(df):
    transformed_df = df \
        .withColumn("TOTAL_PRICE", when(col("O_TOTALPRICE").isNotNull(), col("O_TOTALPRICE").cast(DoubleType())).otherwise(0.0)) \
        .withColumn("SHIP_PRIORITY", when(col("O_SHIPPRIORITY").isNotNull(), col("O_SHIPPRIORITY").cast(IntegerType())).otherwise(1)) \
        .withColumn("CLERK", when(col("O_CLERK").isNotNull(), trim(col("O_CLERK"))).otherwise("Unknown Clerk")) \
        .withColumn("COMMENT", when(col("O_COMMENT").isNotNull(), trim(col("O_COMMENT"))).otherwise("No Comment")) \
        .withColumn("ORDER_DATE", when(col("O_ORDERDATE").isNotNull(), to_date(col("O_ORDERDATE"), 'd/M/yyyy')).otherwise("1970-01-01")) \
        .withColumn("ORDER_STATUS", when(col("O_ORDERSTATUS").isNotNull(), upper(col("O_ORDERSTATUS"))).otherwise("UNKNOWN")) \
        .withColumn("ORDER_PRIORITY", when(col("O_ORDERPRIORITY").isNotNull(), upper(col("O_ORDERPRIORITY"))).otherwise("LOW")) \
        .withColumn("CUST_KEY", when(col("O_CUSTKEY").isNotNull(), col("O_CUSTKEY").cast(IntegerType())).otherwise(-1)) \
        .withColumn("ORDER_KEY", when(col("O_ORDERKEY").isNotNull(), col("O_ORDERKEY").cast(IntegerType())).otherwise(-1)) \
        .drop("O_TOTALPRICE", "O_SHIPPRIORITY", "O_CLERK", "O_COMMENT", "O_ORDERDATE", "O_ORDERSTATUS", "O_ORDERPRIORITY", "O_CUSTKEY", "O_ORDERKEY")
    return transformed_df

# LINEITEMS Table Transformation
def transform_lineitem(df):
    transformed_df = df \
        .withColumn("LINEITEM_KEY", when(col("L_LINENUMBER").isNotNull(), col("L_LINENUMBER").cast(IntegerType())).otherwise(-1)) \
        .withColumn("ORDER_KEY", when(col("L_ORDERKEY").isNotNull(), col("L_ORDERKEY").cast(IntegerType())).otherwise(-1)) \
        .withColumn("PART_KEY", when(col("L_PARTKEY").isNotNull(), col("L_PARTKEY").cast(IntegerType())).otherwise(-1)) \
        .withColumn("SUPP_KEY", when(col("L_SUPPKEY").isNotNull(), col("L_SUPPKEY").cast(IntegerType())).otherwise(-1)) \
        .withColumn("QUANTITY", when(col("L_QUANTITY").isNotNull(), col("L_QUANTITY").cast(DoubleType())).otherwise(0.0)) \
        .withColumn("EXTENDED_PRICE", when(col("L_EXTENDEDPRICE").isNotNull(), col("L_EXTENDEDPRICE").cast(DoubleType())).otherwise(0.0)) \
        .withColumn("DISCOUNT", when(col("L_DISCOUNT").isNotNull(), col("L_DISCOUNT").cast(DoubleType())).otherwise(0.0)) \
        .withColumn("TAX", when(col("L_TAX").isNotNull(), col("L_TAX").cast(DoubleType())).otherwise(0.0)) \
        .withColumn("RETURN_FLAG", when(col("L_RETURNFLAG").isNotNull(), upper(trim(col("L_RETURNFLAG")))).otherwise("N")) \
        .withColumn("LINE_STATUS", when(col("L_LINESTATUS").isNotNull(), upper(trim(col("L_LINESTATUS")))).otherwise("O")) \
        .withColumn("SHIP_DATE", when(col("L_SHIPDATE").isNotNull(), to_date(col("L_SHIPDATE"), 'd/M/yyyy')).otherwise("1970-01-01")) \
        .withColumn("COMMIT_DATE", when(col("L_COMMITDATE").isNotNull(), to_date(col("L_COMMITDATE"), 'd/M/yyyy')).otherwise("1970-01-01")) \
        .withColumn("RECEIPT_DATE", when(col("L_RECEIPTDATE").isNotNull(), to_date(col("L_RECEIPTDATE"), 'd/M/yyyy')).otherwise("1970-01-01")) \
        .withColumn("SHIP_INSTRUCTIONS", when(col("L_SHIPINSTRUCT").isNotNull(), trim(col("L_SHIPINSTRUCT"))).otherwise("NONE")) \
        .withColumn("SHIP_MODE", when(col("L_SHIPMODE").isNotNull(), upper(trim(col("L_SHIPMODE")))).otherwise("UNKNOWN")) \
        .withColumn("COMMENT", when(col("L_COMMENT").isNotNull(), trim(col("L_COMMENT"))).otherwise("No Comment")) \
        .drop("L_LINENUMBER", "L_ORDERKEY", "L_PARTKEY", "L_SUPPKEY", "L_QUANTITY", "L_EXTENDEDPRICE", "L_DISCOUNT", "L_TAX", "L_RETURNFLAG", "L_LINESTATUS", "L_SHIPDATE", "L_COMMITDATE", "L_RECEIPTDATE", "L_SHIPINSTRUCT", "L_SHIPMODE", "L_COMMENT")
    return transformed_df

# PART Table Transformation
def transform_part(df):
    transformed_df = df \
        .withColumn("PART_KEY", when(col("P_PARTKEY").isNotNull(), col("P_PARTKEY").cast(IntegerType())).otherwise(-1)) \
        .withColumn("NAME", when(col("P_NAME").isNotNull(), lower(trim(col("P_NAME")))).otherwise("unknown")) \
        .withColumn("MFGR", when(col("P_MFGR").isNotNull(), lower(trim(col("P_MFGR")))).otherwise("unknown")) \
        .withColumn("BRAND", when(col("P_BRAND").isNotNull(), lower(trim(col("P_BRAND")))).otherwise("unknown")) \
        .withColumn("TYPE", when(col("P_TYPE").isNotNull(), lower(trim(col("P_TYPE")))).otherwise("unknown")) \
        .withColumn("SIZE", when(col("P_SIZE").isNotNull(), col("P_SIZE").cast(IntegerType())).otherwise(0)) \
        .withColumn("CONTAINER", when(col("P_CONTAINER").isNotNull(), lower(trim(col("P_CONTAINER")))).otherwise("unknown")) \
        .withColumn("RETAIL_PRICE", when(col("P_RETAILPRICE").isNotNull(), col("P_RETAILPRICE").cast(DoubleType())).otherwise(0.0)) \
        .withColumn("COMMENT", when(col("P_COMMENT").isNotNull(), trim(col("P_COMMENT"))).otherwise("No Comment")) \
        .drop("P_PARTKEY", "P_NAME", "P_MFGR", "P_BRAND", "P_TYPE", "P_SIZE", "P_CONTAINER", "P_RETAILPRICE", "P_COMMENT")
    return transformed_df

# PARTSUPP Table Transformation
def transform_partsupp(df):
    transformed_df = df \
        .withColumn("PART_KEY", when(col("PS_PARTKEY").isNotNull(), col("PS_PARTKEY").cast(IntegerType())).otherwise(-1)) \
        .withColumn("SUPP_KEY", when(col("PS_SUPPKEY").isNotNull(), col("PS_SUPPKEY").cast(IntegerType())).otherwise(-1)) \
        .withColumn("AVAIL_QTY", when(col("PS_AVAILQTY").isNotNull(), col("PS_AVAILQTY").cast(IntegerType())).otherwise(0)) \
        .withColumn("SUPPLY_COST", when(col("PS_SUPPLYCOST").isNotNull(), col("PS_SUPPLYCOST").cast(DoubleType())).otherwise(0.0)) \
        .withColumn("COMMENT", when(col("PS_COMMENT").isNotNull(), trim(col("PS_COMMENT"))).otherwise("No Comment")) \
        .drop("PS_PARTKEY", "PS_SUPPKEY", "PS_AVAILQTY", "PS_SUPPLYCOST", "PS_COMMENT")
    return transformed_df
