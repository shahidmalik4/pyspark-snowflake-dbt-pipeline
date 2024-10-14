SELECT
    o.ORDER_DATE,
    SUM(o.TOTAL_PRICE) AS total_revenue,
    COUNT(o.ORDER_KEY) AS total_orders
FROM {{ ref('fact_orders') }} o
JOIN {{ ref('dim_customer') }} c ON o.CUST_KEY = c.CUST_KEY
GROUP BY o.ORDER_DATE
ORDER BY o.ORDER_DATE
