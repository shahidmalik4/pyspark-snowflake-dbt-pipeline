{{ config(
    materialized='incremental',
    unique_key='CUST_KEY'
) }}


WITH customer AS (
    SELECT * FROM {{ source('transform', 'customer_transformed') }}
)
SELECT
    NAME,
    PHONE,
    CUST_KEY,
    ADDRESS,
    NATION_KEY,
    COMMENT,
    ACCTBAL,
    MKTSEGMENT
FROM customer
