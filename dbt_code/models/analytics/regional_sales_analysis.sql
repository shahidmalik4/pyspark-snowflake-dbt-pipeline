SELECT
    r.NAME AS region_name,
    SUM(o.TOTAL_PRICE) AS total_revenue
FROM {{ ref('fact_orders') }} o
JOIN {{ ref('dim_customer') }} c ON o.CUST_KEY = c.CUST_KEY
JOIN {{ ref('dim_nation') }} n ON c.NATION_KEY = n.NATION_KEY
JOIN {{ ref('dim_region') }} r ON n.REGION_KEY = r.REGION_KEY
GROUP BY r.NAME
ORDER BY total_revenue DESC
