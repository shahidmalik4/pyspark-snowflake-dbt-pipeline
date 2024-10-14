{{ config(
    materialized='incremental',
    unique_key='NATION_KEY'
) }}


WITH nation AS (
    SELECT * FROM {{ source('transform', 'nation_transformed') }}
)
SELECT
    NAME,
    REGION_KEY,
    COMMENT,
    NATION_KEY
FROM nation


