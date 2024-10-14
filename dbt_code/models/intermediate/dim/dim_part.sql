{{ config(
    materialized='incremental',
    unique_key='PART_KEY'
) }}


WITH part AS (
    SELECT * FROM {{ source('transform', 'part_transformed') }}
)
SELECT
    SIZE,
    CONTAINER,
    BRAND,
    MFGR,
    RETAIL_PRICE,
    COMMENT,
    TYPE,
    PART_KEY,
    NAME
FROM part