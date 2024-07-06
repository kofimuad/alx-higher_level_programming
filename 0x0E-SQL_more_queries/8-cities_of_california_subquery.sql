-- List all cities
-- Databse name would be passed into command
SELECT id, name FROM cities
WHERE state_id IN (SELECT id FROM states WHERE name='California')
ORDER BY id;
