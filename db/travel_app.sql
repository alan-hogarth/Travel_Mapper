DROP TABLE visits;
DROP TABLE sights;
DROP TABLE cities;
DROP TABLE countries;

CREATE TABLE sights (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE cities (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE countries (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE visits (
  id SERIAL PRIMARY KEY,
  sight_id INT REFERENCES sights(id) ON DELETE CASCADE,
  city_id INT REFERENCES cities(id) ON DELETE CASCADE,
  country_id INT REFERENCES countries(id) ON DELETE CASCADE,
  to_visit BOOLEAN
);