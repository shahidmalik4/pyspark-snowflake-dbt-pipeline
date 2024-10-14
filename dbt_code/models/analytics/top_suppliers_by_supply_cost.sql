WITH ranked_suppliers AS (
    SELECT
        s.NAME AS supplier_name,
        ps.SUPPLY_COST,
        RANK() OVER (ORDER BY ps.SUPPLY_COST DESC) AS supplier_rank
    FROM {{ ref('fact_partsupp') }} ps
    JOIN {{ ref('dim_supplier') }} s ON ps.SUPP_KEY = s.SUPP_KEY
)
SELECT *
FROM ranked_suppliers
WHERE supplier_rank <= 10
