{{ config(
    materialized='incremental',
    unique_key='SUPP_KEY'
) }}


WITH supplier AS (
    SELECT * FROM {{ source('transform', 'supplier_transformed') }}
)
SELECT
    PHONE,
    ADDRESS,
    ACCTBAL,
    SUPP_KEY,
    NAME,
    NATION_KEY,
    COMMENT
FROM supplier


