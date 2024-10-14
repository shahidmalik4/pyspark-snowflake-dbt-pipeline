{{ config(
    materialized='incremental'
) }}


WITH partsupp AS (
    SELECT * FROM {{ source('transform', 'partsupp_transformed') }}
)
SELECT
    PART_KEY,
    SUPP_KEY,
    AVAIL_QTY,
    SUPPLY_COST,
    COMMENT
FROM partsupp
