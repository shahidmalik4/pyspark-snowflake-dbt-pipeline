SELECT
    p.NAME AS product_name,
    SUM(l.EXTENDED_PRICE) AS total_revenue
FROM {{ ref('fact_lineitem') }} l
JOIN {{ ref('dim_part') }} p ON l.PART_KEY = p.PART_KEY
GROUP BY p.NAME
ORDER BY total_revenue DESC
LIMIT 10
