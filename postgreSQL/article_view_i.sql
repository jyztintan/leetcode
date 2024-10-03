-- Write your PostgreSQL query statement below
SELECT DISTINCT v.viewer_id as id
FROM views v
WHERE v.author_id = v.viewer_id