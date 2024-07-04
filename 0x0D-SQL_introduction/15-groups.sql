-- List number of records with the same score on second_table
-- Record should be ordered by descending order
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC
