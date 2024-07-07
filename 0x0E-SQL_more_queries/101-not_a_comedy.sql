-- A list of shows from the database that are not comedy shows
SELECT DISTINCT t.title
FROM tv_shows AS t 
LEFT JOIN tv_show_genres AS s
ON t.id = s.show_id
LEFT JOIN tv_genres AS g
ON g.id = s.genre_id
WHERE t.title NOT IN (
	SELECT t.title
	FROM tv_shows AS t
	JOIN tv_show_genres AS s
	ON t.id = s.show_id
	JOIN tv_genres AS g
	ON g.id = s.genre_id
	WHERE g.name = 'Comedy')
ORDER BY t.title;
