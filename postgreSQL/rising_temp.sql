-- Write your PostgreSQL query statement below
SELECT w1.id as Id
FROM weather w1, weather w2
WHERE w1.temperature > w2.temperature
AND w1.recordDate = w2.recordDate + INTERVAL '1 day'