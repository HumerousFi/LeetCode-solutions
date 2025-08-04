# Write your MySQL query statement below
SELECT tweet_id
FROM Tweets
WHERE NOT LENGTH(content) <= 15;