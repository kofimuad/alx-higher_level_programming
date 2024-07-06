-- Use count to see number of shows
SELECT tv.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres AS tv
JOIN tv_show_genres AS tsg
WHERE tv.id = tsg.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
