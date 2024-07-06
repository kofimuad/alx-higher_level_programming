-- Joining two tables using only select
SELECT c.id, c.name, s.name
FROM cities AS c, states AS s
WHERE c.state_id=s.id
ORDER BY c.id;
