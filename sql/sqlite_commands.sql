-- link: https://www.w3schools.com/sql/

-- Creating a table with some types, primary key, and attributes
-- Constraints (CHECK, DEFAULT, NOT NULL, PRIMARY KEY, UNIQUE, ... )
CREATE TABLE flights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    duration INTEGER NOT NULL
);

-- Insert data
INSERT INTO flights 
    (origin, destination, duration)
    VALUES ("Incheon", "New York", 840);

-- Select data
SELECT * 
FROM flights; 

SELECT origin, destination FROM flights; 

SELECT * 
FROM flights
WHERE id = 1; 

SELECT * FROM flights WHERE duration > 500 OR destination = "Paris"; 

-- Wild card of %, where there is an a 
SELECT * FROM flights WHERE origin LIKE "%a%"; 

-- Update
UPDATE flights 
SET duration = 430 
WHERE origin = "New York" 
AND destination = "London"; 

-- Delete (LIMIT, ORDER BY, GROUP BY, HAVING) 
DELETE FROM flights WHERE destination = "Incheon"

-- Join 
-- Inner join: Match on both sides 
-- Left outer join: Only on the left side
-- Right outer join: Only on the right side
-- Outer join: Both 
SELECT first_name, origin, destination 
FROM flights JOIN passengers 
ON passengers.flight_id = flights.id; 