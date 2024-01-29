DROP DATABASE IF EXISTS tuneseek;

CREATE DATABASE tuneseek;

\c tuneseek

CREATE TABLE users
(
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    full_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);


CREATE TABLE artists
(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE genre
(
    id SERIAL PRIMARY KEY,
    category TEXT NOT NULL
);

CREATE TABLE songs
(
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    lyrics TEXT NOT NULL,
    released_on DATE NOT NULL,
    artist_id INTEGER REFERENCES artists,
    genre_id INTEGER REFERENCES genre
);