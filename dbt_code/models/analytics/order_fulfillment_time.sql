SELECT
    o.ORDER_KEY,
    DATEDIFF(day, o.ORDER_DATE, l.SHIP_DATE) AS fulfillment_time
FROM {{ ref('fact_orders') }} o
JOIN {{ ref('fact_lineitem') }} l ON o.ORDER_KEY = l.ORDER_KEY
WHERE l.SHIP_DATE IS NOT NULL
