SELECT s.user_id, COALESCE(ROUND(subquery1.confirmed / subquery2.total::numeric, 2), 0) AS confirmation_rate
FROM signups s LEFT JOIN (
    SELECT c.user_id, COUNT(*) AS confirmed
    FROM confirmations c
    WHERE c.action = 'confirmed'
    GROUP BY c.user_id) subquery1 ON s.user_id = subquery1.user_id
LEFT JOIN (
    SELECT c.user_id, COUNT(*) AS total
    FROM confirmations c
    GROUP BY c.user_id
) subquery2 ON s.user_id = subquery2.user_id