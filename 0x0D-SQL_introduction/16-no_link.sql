-- List all records from second table with some exceptions
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
