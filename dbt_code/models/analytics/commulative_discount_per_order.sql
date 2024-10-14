SELECT
    l.ORDER_KEY,
    l.LINEITEM_KEY,
    l.DISCOUNT,
    SUM(l.DISCOUNT) OVER (PARTITION BY l.ORDER_KEY ORDER BY l.LINEITEM_KEY) AS cumulative_discount
FROM {{ ref('fact_lineitem') }} l
ORDER BY l.ORDER_KEY, l.LINEITEM_KEY
