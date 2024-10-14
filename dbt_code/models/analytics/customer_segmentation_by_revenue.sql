SELECT
    c.MKTSEGMENT,
    SUM(o.TOTAL_PRICE) AS total_revenue
FROM {{ ref('fact_orders') }} o
JOIN {{ ref('dim_customer') }} c ON o.CUST_KEY = c.CUST_KEY
GROUP BY c.MKTSEGMENT
ORDER BY total_revenue DESC
