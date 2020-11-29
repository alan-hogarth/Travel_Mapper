DROP TABLE visits;
DROP TABLE users;
DROP TABLE cities;
DROP TABLE countries;

CREATE TABLE users (
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
  city_id INT REFERENCES cities(id) ON DELETE CASCADE,
  country_id INT REFERENCES countries(id) ON DELETE CASCADE,
  to_visit BOOLEAN
);