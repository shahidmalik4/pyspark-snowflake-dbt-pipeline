SELECT
    s.NAME AS supplier_name,
    SUM(ps.AVAIL_QTY) AS total_qty_supplied,
    AVG(ps.SUPPLY_COST) AS avg_supply_cost
FROM {{ ref('fact_partsupp') }} ps
JOIN {{ ref('dim_supplier') }} s ON ps.SUPP_KEY = s.SUPP_KEY
GROUP BY s.NAME
ORDER BY total_qty_supplied DESC
