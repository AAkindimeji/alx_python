SELECT cities.name 
FROM cities 
JOIN states ON cities.state_id = states.id 
WHERE states.name = 'Texas' 
ORDER BY cities.id ASC;
