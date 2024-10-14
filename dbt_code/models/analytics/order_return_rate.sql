SELECT
    l.ORDER_KEY,
    COUNT(CASE WHEN l.RETURN_FLAG = 'R' THEN 1 END) / COUNT(*) * 100 AS return_rate
FROM {{ ref('fact_lineitem') }} l
GROUP BY l.ORDER_KEY
ORDER BY return_rate DESC
