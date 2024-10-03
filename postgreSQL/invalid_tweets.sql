-- Write your PostgreSQL query statement below
SELECT t.tweet_id
FROM tweets t
WHERE LENGTH(t.content) > 15