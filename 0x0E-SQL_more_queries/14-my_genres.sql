-- List all genres of the show Dexter
SELECT g.name FROM tv_genres AS g
INNER JOIN tv_show_genres AS s
ON s.genre_id = g.id
INNER JOIN tv_shows AS t
ON t.id = s.show_id
WHERE t.title = 'Dexter'
ORDER BY g.name;
