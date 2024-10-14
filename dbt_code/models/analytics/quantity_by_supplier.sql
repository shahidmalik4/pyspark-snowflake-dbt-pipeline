SELECT
    s.NAME AS supplier_name,
    ps.AVAIL_QTY,
    SUM(ps.AVAIL_QTY) OVER () AS total_qty,
    (ps.AVAIL_QTY / SUM(ps.AVAIL_QTY) OVER ()) * 100 AS supplier_contribution
FROM {{ ref('fact_partsupp') }} ps
JOIN {{ ref('dim_supplier') }} s ON ps.SUPP_KEY = s.SUPP_KEY