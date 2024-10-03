-- Write your PostgreSQL query statement below
SELECT c.name
FROM customer c
WHERE c.referee_id is NULL
OR c.referee_id <> 2;