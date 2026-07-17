-- Write your query below
SELECT s.seller_name
FROM seller s
LEFT JOIN orders o
ON s.seller_id=o.seller_id 
    AND o.sale_date >= '2020-01-01'
    AND o.sale_date <= '2020-12-31'
WHERE o.seller_id IS NULL
ORDER BY s.seller_name ASC