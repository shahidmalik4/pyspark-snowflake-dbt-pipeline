WITH ranked_products AS (
    SELECT
        p.NAME AS product_name,
        SUM(l.EXTENDED_PRICE) AS total_sales,
        DENSE_RANK() OVER (ORDER BY SUM(l.EXTENDED_PRICE) DESC) AS product_rank
    FROM {{ ref('fact_lineitem') }} l
    JOIN {{ ref('dim_part') }} p ON l.PART_KEY = p.PART_KEY
    GROUP BY p.NAME
)
SELECT
    product_name,
    total_sales,
    product_rank
FROM ranked_products
WHERE product_rank <= 10
ORDER BY total_sales DESC
