-- Basically, a script that creates a list of all records that have been linked to another table records.
SELECT tv.title, tsg.genre_id
FROM tv_shows AS tv, tv_show_genres AS tsg
WHERE tsg.show_id=tv.id
ORDER BY tv.title, tsg.genre_id;
