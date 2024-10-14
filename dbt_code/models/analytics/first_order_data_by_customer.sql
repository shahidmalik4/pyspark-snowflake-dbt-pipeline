SELECT
    c.CUST_KEY,
    c.NAME AS customer_name,
    MIN(o.ORDER_DATE) AS first_order_date,
    COUNT(o.ORDER_KEY) AS total_orders
FROM {{ ref('fact_orders') }} o
JOIN {{ ref('dim_customer') }} c ON o.CUST_KEY = c.CUST_KEY
GROUP BY c.CUST_KEY, c.NAME
ORDER BY first_order_date
