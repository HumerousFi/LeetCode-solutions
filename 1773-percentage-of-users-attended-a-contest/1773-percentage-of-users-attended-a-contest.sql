# Write your MySQL query statement below
SELECT r.contest_id , ROUND(COUNT(r.contest_id)*100/(SELECT COUNT(*) FROM Users),2) AS percentage
FROM Users AS u RIGHT JOIN Register AS r ON u.user_id = r.user_id
GROUP BY r.contest_id
ORDER BY percentage DESC , r.contest_id ASC