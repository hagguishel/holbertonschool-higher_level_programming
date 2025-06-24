-- 15 Number by
SELECT score,
	COUNT(score) AS Number
FROM second_table
GROUP BY score
ORDER BY Number DESC