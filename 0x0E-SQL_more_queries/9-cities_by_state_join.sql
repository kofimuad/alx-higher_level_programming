SELECT c.id, c.name, s.name
FROM cities AS c, states as s
WHERE c.state_id=s.id
ORDER BY c.id;
