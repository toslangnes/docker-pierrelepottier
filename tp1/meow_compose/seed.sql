CREATE DATABASE IF NOT EXISTS meow;
USE meow;

CREATE TABLE IF NOT EXISTS users
(
    id
    INT
    AUTO_INCREMENT
    PRIMARY
    KEY,
    name
    VARCHAR
(
    255
) NOT NULL,
    favorite_insult TEXT
    );

INSERT INTO users (name, favorite_insult)
VALUES ('Alice', 'You silly cat!'),
       ('Bob', 'Meow you kidding me!'),
       ('Charlie', 'Stop paw-sing around!'),
       ('Diana', 'You fur-getful feline!'),
       ('Eve', 'Purr-haps think twice!');