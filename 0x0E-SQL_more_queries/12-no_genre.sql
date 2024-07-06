-- Using where atfer ON
SELECT tv.title, tsg.genre_id
FROM tv_shows AS tv
LEFT JOIN tv_show_genres AS tsg
ON tv.id=tsg.show_id
WHERE tsg.genre_id IS NULL
ORDER BY tv.title, tsg.genre_id;
