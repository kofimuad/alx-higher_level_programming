-- List all genres in the database that are not linked to Dexter
SELECT DISTINCT g.name
FROM tv_genres AS g
JOIN tv_show_genres AS s
ON g.id = s.genre_id
JOIN tv_shows AS t
ON t.id = s.show_id
WHERE g.name NOT IN (
	SELECT g.name
	FROM tv_genres AS g
	JOIN tv_show_genres AS s
	ON g.id = s.genre_id
	JOIN tv_shows AS t
	ON t.id = s.show_id
	WHERE t.id = 8)
ORDER BY g.name;
