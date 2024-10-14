SELECT
    o.CUST_KEY,
    c.NAME AS customer_name,
    o.ORDER_DATE,
    o.TOTAL_PRICE,
    SUM(o.TOTAL_PRICE) OVER (PARTITION BY o.CUST_KEY ORDER BY o.ORDER_DATE) AS running_total_sales
FROM {{ ref('fact_orders') }} o
JOIN {{ ref('dim_customer') }} c ON o.CUST_KEY = c.CUST_KEY
ORDER BY o.CUST_KEY, o.ORDER_DATE
