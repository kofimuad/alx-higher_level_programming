-- List all shows and all genres linked to that show
SELECT t.title, g.name
FROM tv_shows AS t
LEFT JOIN tv_show_genres AS s
ON t.id=s.show_id
LEFT JOIN tv_genres AS g
ON g.id = s.genre_id
ORDER BY title, name;
