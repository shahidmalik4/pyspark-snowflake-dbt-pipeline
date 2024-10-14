WITH rolling_order_counts AS (
    SELECT
        o.CUST_KEY,
        c.NAME AS customer_name,
        o.ORDER_DATE,
        COUNT(o.ORDER_KEY) OVER (
            PARTITION BY o.CUST_KEY 
            ORDER BY o.ORDER_DATE 
            ROWS BETWEEN 30 PRECEDING AND CURRENT ROW
        ) AS rolling_order_count
    FROM {{ ref('fact_orders') }} o
    LEFT JOIN {{ ref('dim_customer') }} c ON o.CUST_KEY = c.CUST_KEY
    WHERE o.ORDER_DATE IS NOT NULL
)
SELECT *
FROM rolling_order_counts
ORDER BY CUST_KEY, ORDER_DATE
