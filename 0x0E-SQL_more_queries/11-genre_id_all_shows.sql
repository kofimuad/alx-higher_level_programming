-- Using left join to still list tv shows that dont have genres.
SELECT tv.title, tsg.genre_id
FROM tv_shows AS tv
LEFT JOIN tv_show_genres AS tsg
ON tv.id=tsg.show_id
ORDER BY tv.title, tsg.genre_id;
