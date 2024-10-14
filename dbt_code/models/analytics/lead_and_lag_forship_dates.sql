SELECT
    l.ORDER_KEY,
    l.SHIP_DATE,
    LAG(l.SHIP_DATE) OVER (ORDER BY l.ORDER_KEY) AS previous_ship_date,
    LEAD(l.SHIP_DATE) OVER (ORDER BY l.ORDER_KEY) AS next_ship_date
FROM {{ ref('fact_lineitem') }} l
ORDER BY l.ORDER_KEY
