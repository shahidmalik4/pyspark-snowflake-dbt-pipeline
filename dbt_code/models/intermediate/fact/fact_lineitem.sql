{{ config(
    materialized='incremental',
    unique_key='LINEITEM_KEY'
) }}


WITH lineitem AS (
    SELECT * FROM {{ source('transform', 'lineitem_transformed') }}
)
SELECT
    RECEIPT_DATE,
    PART_KEY,
    COMMIT_DATE,
    COMMENT,
    SHIP_DATE,
    QUANTITY,
    SHIP_MODE,
    SUPP_KEY,
    TAX,
    DISCOUNT,
    LINE_STATUS,
    LINEITEM_KEY,
    EXTENDED_PRICE,
    RETURN_FLAG,
    ORDER_KEY,
    SHIP_INSTRUCTIONS
FROM lineitem
