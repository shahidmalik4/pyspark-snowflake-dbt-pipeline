{{ config(
    materialized='incremental',
    unique_key='ORDER_KEY'
) }}


WITH orders AS (
    SELECT * FROM {{ source('transform', 'orders_transformed') }}
)
SELECT
    SHIP_PRIORITY,
    CUST_KEY,
    ORDER_KEY,
    TOTAL_PRICE,
    COMMENT,
    ORDER_STATUS,
    ORDER_PRIORITY,
    ORDER_DATE,
    CLERK
FROM orders
