-- a sub query script
SELECT * FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'Califonia') ORDER BY id;
