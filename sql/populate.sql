CREATE TABLE flights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    duration INTEGER NOT NULL
);

CREATE TABLE flights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origin_id INTEGER NOT NULL,
    destination_id INTEGER NOT NULL,
    duration INTEGER NOT NULL
);

CREATE TABLE airports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL,
    city INTEGER NOT NULL
);

CREATE TABLE passengers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name INTEGER NOT NULL,
    flight_id INTEGER NOT NULL
);

CREATE TABLE people (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name INTEGER NOT NULL
);



INSERT INTO flights 
    (origin, destination, duration)
    VALUES 
    ("New York", "London", 415),
    ("Shanghai", "Paris", 760),
    ("Istanbul", "Tokyo", 700),
    ("New York", "Paris", 435),
    ("Moscow", "Paris", 245),
    ("Lima", "New York", 455);

-- With ids
INSERT INTO flights
    (origin_id, destination_id, duration)
    VALUES 
    (1, 4, 415),
    (2, 7, 760),
    (3, 8, 700),
    (1, 7, 435),
    (5, 7, 245),
    (6, 1, 455),

INSERT INTO airports 
    (code, city)
    VALUES ("JFK", "New York"),
    ("PVG", "Shanghai"),
    ("IST", "Istanbul"),
    ("LHR", "London"),
    ("SVO", "Moscow"),
    ("LIM", "Lima"),
    ("CDG", "Paris"),
    ("NRT", "Tokyo"),
    ("ICN", "Incheon");

-- Problem is stroign only one flight id, where they might have multiples 
-- Make a separate table for people and another table that relates people and their flights 
INSERT INTO passengers 
    (first_name, last_name, flight_id) VALUES
    ("Harry", "Potter", 1),
    ("Ron", "Weasley", 1),
    ("Hermione", "Granger", 2),
    ("Draco", "Malfoy", 4),
    ("Luna", "Lovegood", 6),
    ("Ginny", "Weasley", 6);

INSERT INTO passengers 
    (person_id, flight_id) VALUES 
    (1, 1),
    (2, 1), 
    (2, 4),
    (3, 2),
    (4, 4),
    (5, 6),
    (6, 6);

INSERT INTO people
    (first_name, last_name) VALUES
    ("Harry", "Potter"),
    ("Ron", "Weasley"),
    ("Hermione", "Granger"),
    ("Draco", "Malfoy"),
    ("Luna", "Lovegood"),
    ("Ginny", "Weasley");