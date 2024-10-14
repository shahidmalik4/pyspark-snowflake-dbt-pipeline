{{ config(
    materialized='incremental',
    unique_key='REGION_KEY'
) }}


WITH region AS (
    SELECT * FROM {{ source('transform', 'region_transformed') }}
)
SELECT
    NAME,
    COMMENT,
    REGION_KEY
FROM region


