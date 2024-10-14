WITH item_pairs AS (
    SELECT
        l1.ORDER_KEY,
        l1.PART_KEY AS item1,
        l2.PART_KEY AS item2
    FROM {{ ref('fact_lineitem') }} l1
    JOIN {{ ref('fact_lineitem') }} l2 ON l1.ORDER_KEY = l2.ORDER_KEY
    WHERE l1.PART_KEY < l2.PART_KEY
)
SELECT
    item1,
    item2,
    COUNT(*) AS pair_count
FROM item_pairs
GROUP BY item1, item2
ORDER BY pair_count DESC
LIMIT 10
