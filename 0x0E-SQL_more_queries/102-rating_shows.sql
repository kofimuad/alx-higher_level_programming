-- List all shows from database by rating
SELECT t.title, SUM(r.rate) AS rating
FROM tv_shows AS t
JOIN tv_show_ratings AS r
ON r.show_id = t.id
GROUP BY t.title
ORDER BY rating DESC;
